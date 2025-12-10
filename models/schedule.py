from Datalayer.data_api import DataAPI
from models.team import Team
from models.tournament import Tournament
from models.match import Match
from datetime import *
import math
import random

class Schedule():
    def __init__(self, tournament: Tournament):
        self._data_api = DataAPI()

        self._tournament: Tournament = tournament
        self._all_teams: list = self._data_api.get_all_teams()
        self._teams: list = self.get_tournament_teams()
        self._number_of_teams: int = len(self._teams)
        self._number_of_games: int = self._number_of_teams - 1
        self._number_of_rounds: int = self.get_number_of_rounds()
        self._tournament_days: int = self.get_tournament_days()
        self._slots_per_day: int = self.get_slots_per_day()
        self._slot_times: list[datetime] = self.get_slot_times()
        self._game_number: int = 0
        self.create_playoffs()
        self.create_rounds()

    def get_tournament_teams(self):
        '''Creates a list of all teams in tournament'''

        teams = []
        for team in self._all_teams:
            team: Team
            if self._tournament.id in team.tour_ID:
                teams.append(team.name)

        random.shuffle(teams)
        return teams
    
    def get_number_of_rounds(self):
        '''Calculates number of rounds needed for tournament schedule'''

        rounds = 0
        while 2 ** rounds <= self._number_of_teams:
            rounds += 1

        return rounds - 1
    
    def get_tournament_days(self):
        '''Calculates the length of tournament'''

        start = self._tournament.start_date.split("-")
        end = self._tournament.end_date.split("-")

        # Turn string date into datetime object
        start_date = date(int(start[2]), int(start[1]), int(start[0]))
        end_date = date(int(end[2]), int(end[1]), int(end[0]))

        self.current_date = start_date

        dates = end_date - start_date

        return dates.days + 1

    def get_slots_per_day(self):
        '''Generates number of slots per day'''

        num_servers = len(self._tournament.servers)
        games_per_day = math.ceil(self._number_of_games / self._tournament_days)
        server_slots = math.ceil(games_per_day / num_servers)
        round_slots = math.floor(self._number_of_rounds / self._tournament_days)

        print(games_per_day, num_servers, self._number_of_rounds, self._tournament_days)
        print(server_slots)
        print(round_slots)
        return server_slots + round_slots

    def get_slot_times(self):
        '''Generates times for game slots'''

        slot_times = []
        difference = 13 / (self._slots_per_day + 1)

        hours = math.floor(difference)

        minutes = round((difference - math.floor(difference)) * 60)

        addition = timedelta(hours = hours, minutes = minutes)

        current_date = self.current_date
        current_time = time(8)
        current = datetime.combine(current_date, current_time) + addition
        for _ in range(self._slots_per_day):
            slot_times.append(current.time())
            current: datetime = current + timedelta(hours = 1, minutes = 30)

        return slot_times

    def create_playoffs(self):
        '''Generates playoff round if needed'''

        self.time_location = 0

        if self._number_of_teams > 2 ** self._number_of_rounds:
            excess = self._number_of_teams - (2 ** self._number_of_rounds)

            for team in range((self._number_of_teams - 1),
                            (self._number_of_teams - (excess * 2)),
                            (-2)):
                
                team_a: str = self._teams[team]
                team_b: str = self._teams[team - 1]
                server: str = self._tournament.servers[(self._game_number % len(self.tournament.servers)) - 1]

                _match = Match(self._game_number + 1, self.tournament.id, "Playoffs", team_a, team_b,
                            self.current_date, self.slot_times[self.time_location], server,
                            )

                self._data_api.add_match(_match)

                self._teams[team - 1] = f"Winner of game {self._game_number + 1}"
                self._teams.remove(team_a)

                self._game_number += 1

                if (self._game_number % len(self._tournament.servers)) == len(self._tournament.servers):
                    if self._slot_times[-1] == self._slot_times[self.time_location]:
                        self.time_location = 0
                        self.current_date = self.current_date + timedelta(days = 1)

                    else:
                        self.time_location += 1
        return

    def create_rounds(self):
        '''Generates games for rounds after playoffs, if there is a playoff round'''

        rounds = ("Final", "Semifinal", "Quarterfinal", "Round of 16", "Round of 32", "Round of 64")
        last_round = rounds[self._number_of_rounds - 1]
        time_counter = 0
        self._number_of_teams = len(self._teams)

        for stage in range(self._number_of_rounds):
            for team in range((self._number_of_teams - 1), 0, -2):

                team_a = self._teams[team]
                team_b = self._teams[team - 1]

                if last_round != rounds[self._number_of_rounds - stage - 1]:
                    if self._slot_times[-1] == self._slot_times[self.time_location]:
                        self.time_location = 0
                        time_counter = 0
                        self.current_date = self.current_date + timedelta(days = 1)

                    else:
                        self.time_location += 1
                        time_counter = 0

                _match = Match(self._game_number + 1, self._tournament.id,
                            f"{rounds[self._number_of_rounds - stage - 1]}",
                            team_a, team_b,self.current_date, self._slot_times[self.time_location],
                            self._tournament.servers[(self._game_number % len(self._tournament.servers))]
                            )

                if time_counter == len(self._tournament.servers) - 1:
                    if self._slot_times[-1] == self._slot_times[self.time_location]:
                        self.time_location = 0
                        time_counter = 0
                        self.current_date = self.current_date + timedelta(days = 1)

                    else:
                        self.time_location += 1
                        time_counter = 0
                
                else:
                    time_counter += 1

                last_round = _match.round

                self._data_api.add_match(_match)

                self._teams[team - 1] = f"Winner of game {self._game_number + 1}"
                self._teams.remove(team_a)

                self._game_number += 1

            self._number_of_teams = len(self._teams)

        return
    
