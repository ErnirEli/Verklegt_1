from models.tournament import Tournament
from models.match import Match
from models.team import Team
from Datalayer.data_api import DataAPI
import random



class Schedule():
    def __init__(self, tournament: Tournament):
        self.tournament = tournament
        self._data_api = DataAPI()
        self._all_teams = self._data_api.get_all_teams()
        self.teams: list = self.get_tournament_teams()
        self.number_of_teams = len(self.teams)
        self.number_of_rounds = self.get_number_of_rounds()
        self.game_number = 1

    def get_tournament_teams(self):
        teams = []
        for team in self._all_teams:
            team: Team
            if self.tournament.id in team.tour_IDs:
                teams.append(team.name)

        random.shuffle(teams)
        return teams
    
    def get_number_of_rounds(self):
        rounds = 0
        while 2 ** rounds <= self.number_of_teams:
            rounds += 1

        return rounds - 1

    def create_playoffs(self):
        if self.number_of_teams > 2 ** self.number_of_rounds:
            excess = self.number_of_teams - (2 ** self.number_of_rounds)

            for team in range((self.number_of_teams - 1),
                            (self.number_of_teams - (excess * 2)),
                            (-2)):
                
                team_a = self.teams[team]
                team_b = self.teams[team - 1]

                _match = Match(self.game_number, self.tournament.id, "Playoffs", team_a, team_b)

                self._data_api.add_match(_match)

                self.teams[team - 1] = f"Winner of game {self.game_number}"
                self.teams.remove(team_a)

                self.game_number += 1

        self.number_of_teams = len(self.teams)
        return

    def create_rounds(self):
        rounds = ("Final", "Semifinal", "Quarterfinal", "Round of 16", "Round of 32", "Round of 64")
        for stage in range(self.number_of_rounds):
            for team in range((self.number_of_teams - 1), 0, -2):

                print("Location: ", team)
                print("Range: 0 - ", len(self.teams))
                print("Num: ", self.number_of_teams)


                team_a = self.teams[team]
                team_b = self.teams[team - 1]

                _match = Match(self.game_number, self.tournament.id,
                            f"{rounds[self.number_of_rounds - stage - 1]}",
                            team_a, team_b)

                self._data_api.add_match(_match)

                self.teams[team - 1] = f"Winner of game {self.game_number}"
                self.teams.remove(team_a)

                self.game_number += 1

            self.number_of_teams = len(self.teams)

        print("Jíbbí")
        return


