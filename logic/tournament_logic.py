from Datalayer.data_api import DataAPI
from logic.schedule_logic import ScheduleLogic
from models.tournament import Tournament
from models.team import Team
from models.match import Match
from models.player import Player
from models.club import Club

class TournamentLogic:
    
    def __init__(self) -> None:
        self._data_api = DataAPI()
        self._schedule = ScheduleLogic()


    def list_all_tournaments(self)-> list[Tournament]:
        '''Takes in nothing and returns a list of all existing tournaments of type Tournament'''

        return self._data_api.get_all_tournaments()

    def get_tournament(self, tournament_id: str) -> Tournament:
        '''Takes in tournament ID and returns the torunament of type Torunament.
        Only runs after all validation checks are valid.'''

        tournaments: list = self._data_api.get_all_tournaments()

        for tournament in tournaments:
            tournament: Tournament

            if tournament.id == tournament_id:
                return tournament

    def add_teams(self, teams: list[str], tournament: Tournament) -> Team:
        '''Takes in a list of team names, of type string, and takes in a tournament.
        Adds all teams to the tournament and updates total tournament stats for
        all teams, players and clubs in tournament.
        Runs automatically when a tournament is created and after all calidation checks are valid.'''

        # Gets a list of all players, teams and clubs
        all_teams: list[Team] = self._data_api.get_all_teams()
        players: list[Player] = self._data_api.get_all_players()
        clubs: list[Club] = self._data_api.get_all_clubs()

        tournament_teams: list[Team] = []

        for team in all_teams:

            if team.name in teams:
                # Gets a list of all teams in the tournament
                tournament_teams.append(team)

        for team in tournament_teams:

            # Adds tournament ID to team
            if team.tour_ID == "None":
                team.tour_ID = tournament.id

            else:
                team.tour_ID += " " + tournament.id

            # Adds 1 to total tournaments of all teams in the tournament
            team.tournament += 1

            # Adds 1 to total tournaments of all players in the tournament
            for player in players:
                player: Player

                if player.team_name == team.name:
                    player.tournament += 1

            # Adds 1 to total tournaments of all clubs in the tournament
            for club in clubs:
                club: Club

                if team.club == club.name:
                    club.tournaments += 1

        self._data_api.write_teams(all_teams)
        self._data_api.write_players(players)
        self._data_api.write_clubs(clubs)

        return
        
    def tournament_schedule(self, tournament: Tournament) -> list[Match]:
        '''Takes in a tournament of type Tournament and returns a list of all matches, of type Match, in that tournament'''

        matches: list[Match] = self._data_api.get_all_matches()

        tournament_matches: list[Match] = []

        for match in matches:
            # Checks if mathc is in tournament
            if match.tournament_id == tournament.id:
                tournament_matches.append(match)

        return tournament_matches
    
    def create_tournament(self, tournament_id: str, name: str, venue: str, start_date: str,
                end_date: str, contact: str, contact_email:str,
                contact_number: str, servers: int, team_list: list[str]) -> Tournament:
        '''Takes in id, name, venue, start & end dates, contact, mail & number, servers, for a tournament, all of type string.
        also takes in a list of team names of type string. Creates a tournament using this info and adds all teams from the list to the torunament.
        Only runs after all validation checks are valid.'''

        # Create an instance of the Tournament Classt = None
        new_tournament = Tournament(tournament_id, name, venue, start_date, end_date,
                                    contact, contact_email, contact_number, servers)
        
        # Add teams to tournament
        self.add_teams(team_list, new_tournament)

        #Update tournametn CSV
        self._data_api.add_tournament(new_tournament)

        #Create torunament Schedule
        self._schedule.create_tournament_schedule(new_tournament)
        return

    def tournament_results(self, match: Match) -> None:
        '''Takes in a match of type Match. Finishes the tournament the match belongs to,
        updating the tournament status.
        Also updates Win and Runer up stats for team, player and Club.
        returns nothing.'''

        # Gets a list of all players, teams, clubs and tournaments
        players: list[Player] = self._data_api.get_all_players()
        teams: list[Team] = self._data_api.get_all_teams()
        clubs: list[Club] = self._data_api.get_all_clubs()
        tournaments: list[Tournament] = self._data_api.get_all_tournaments()

        # Updates win and runner up numbers for players
        for player in players:

            if player.team_name == match.team_a or player.team_name == match.team_b:
                if player.team_name == match.winner:
                    player.wins += 1

                else:
                    player.runner_up += 1


        # Updats win and runner up numbers for teams
        for team in teams:

            if team.name == match.team_a or team.name == match.team_b:
                if team.name == match.winner:
                    team.wins += 1

                else:
                    team.runner_up += 1

                # Updates win and runner up numbers for clubs
                for club in clubs:

                        if team.club == club.name:
                            club.wins += 1

        for tournament in tournaments:

            if tournament.id == match.tournament_id:
                tournament.state = True

        
        self._data_api.write_players(players)
        self._data_api.write_teams(teams)
        self._data_api.write_clubs(clubs)
        self._data_api.write_tournament(tournaments)
        return