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
        '''Returns a list of all tournaments, of type Tournament'''

        return self._data_api.get_all_tournaments()


    def get_tournament(self, tournament_id: str) -> Tournament:
        '''Takes in a tournament id, and returns given tournament, of type Tournament'''

        tournaments: list = self._data_api.get_all_tournaments()

        for tournament in tournaments:
            tournament: Tournament

            if tournament.id == tournament_id:
                return tournament


    def add_teams(self, teams: list, tournament: Tournament) -> Team:
        '''Adds tournament ID to al teams in tournament'''

        # Gets a list of all players, teams and clubs
        all_teams: list = self._data_api.get_all_teams()
        players: list = self._data_api.get_all_players()
        clubs: list = self._data_api.get_all_clubs()

        tournament_teams = []

        for team in all_teams:
            team: Team

            if team.name in teams:

                # Gets a list of all teams in the tournament
                tournament_teams.append(team)


        for team in tournament_teams:
            team: Team

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
                    player.tournaments += 1


            # Adds 1 to total tournaments of all clubs in the tournament
            for club in clubs:
                club: Club

                if team.club == club.name:
                    club.tournaments += 1

        self._data_api.write_teams(all_teams)

        return
        
    def tournament_schedule(self, tournament: Tournament) -> list[Match]:
        '''Returns a list of all matches in a tournament'''

        matches: list = self._data_api.get_all_matches()

        tournament_matches = []

        for match in matches:
            match: Match

            # Checks if mathc is in tournament
            if match.tournament_id == tournament.id:
                tournament_matches.append(match)

        return tournament_matches
    
    def create_a_tournament(self, tournament_id: str, name: str, venue: str, start_date: str,
                end_date: str, contact: str, contact_email:str,
                contact_number:str, servers: int, team_list: list = None):
        '''Creates a Torunament'''
        
        # Create an instance of the Tournament Class
        new_tournament = Tournament(tournament_id, name, venue, start_date, end_date,
                                    contact, contact_email, contact_number, servers)
        
        # Add teams to tournament
        self.add_teams(team_list, new_tournament)

        #Update tournametn CSV
        self._data_api.add_tournament(new_tournament)

        #Create torunament Schedule
        self._schedule.create_tournament_schedule(new_tournament)
        return


    def tournament_bracket(self):
        '''?????'''
        return

    def tournament_results(self, match: Match):
        '''Finished tournament and updates winners'''

        # Gets a list of all players, teams, clubs and tournaments
        players = self._data_api.get_all_players()
        teams = self._data_api.get_all_teams()
        clubs = self._data_api.get_all_clubs()
        tournaments = self._data_api.get_all_tournaments()

        # Updates win and runner up numbers for players
        for player in players:
            player: Player

            if player.team_name == match.team_a or player.team_name == match.team_b:
                if player.team_name == match.winner:
                    player.wins += 1

                else:
                    player.runner_up += 1


        # Updats win and runner up numbers for teams
        for team in teams:
            team: Team

            if team.name == match.team_a or team.name == match.team_b:
                if team.name == match.winner:
                    team.wins += 1

                else:
                    team.runner_up += 1

                # Updates win and runner up numbers for clubs
                for club in clubs:
                        club: Club

                        if team.club == club.name:
                            club.wins += 1

        for tournament in tournaments:
            tournament: Tournament

            if tournament.id == match.tournament_id:
                tournament.state = True

        
        self._data_api.write_players(players)
        self._data_api.write_teams(teams)
        self._data_api.write_clubs(clubs)
        self._data_api.write_tournament(tournaments)
        return