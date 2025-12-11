from Datalayer.data_files.player_data import PlayerFiles
from Datalayer.data_files.team_data import TeamFiles
from Datalayer.data_files.match_data import MatchFiles
from Datalayer.data_files.club_data import ClubFiles
from Datalayer.data_files.tournament_data import TournamentFiles
from models.player import Player
from models.team import Team
from models.match import Match
from models.tournament import Tournament
from models.club import Club

class DataAPI():
    def __init__(self):
        self.player_files: PlayerFiles = PlayerFiles()
        self.team_files: TeamFiles = TeamFiles()
        self.match_files: MatchFiles = MatchFiles()
        self.club_files: ClubFiles = ClubFiles()
        self.tournament_files: TournamentFiles = TournamentFiles()


    def get_all_players(self):
        '''Returns a list of all players in player file,
        players are of type "Player"'''

        return self.player_files.read_player()

    def add_player(self, player: Player):
        '''Takes in a player, of type "Player",
        adds the player to the bottom of player file'''

        self.player_files.add_player(player)
        return

    def write_players(self, players: list):
        '''Takes in a list of players, of type "Player",
        rewrites the player file with all players in the list'''

        self.player_files.write_player(players)
        return


    def get_all_teams(self) -> list:
        '''Returns a list of all tems in team file,
        teams are of type "Team"'''

        return self.team_files.read_team()

    def add_team(self, team: Team):
        '''Takes in a team, of type "Team",
        adds the team to the bottom of team file'''

        self.team_files.add_team(team)
        return

    def write_teams(self, teams: list):
        '''Takes in a list of tems, of type "Team",
        rewrites the team file with all teams in the list'''

        self.team_files.write_team(teams)
        return


    def get_all_matches(self):
        '''Returns a list of all matches in match file,
        matches are of type "Match"'''

        return self.match_files.read_match()
    
    def add_match(self, match: Match):
        '''Takes in a match, of type "Match",
        adds the match to the bottom of match file'''
        
        self.match_files.add_match(match)
        return

    def write_match(self, teams: list):
        '''Takes in a list of matches, of type "Match",
        rewrites the match file with all matches in the list'''
        
        self.match_files.write_match(teams)
        return


    def get_all_clubs(self) -> list:
        '''Returns a list of all clubs in club file,
        clubs are of type "Club"'''
        
        return self.club_files.read_club()
    
    def add_club(self, club: Club):
        '''Takes in a club, of type "Club",
        adds the club to the bottom of club file'''
        
        self.club_files.add_club(club)
        return

    def write_clubs(self, clubs: list):
        '''Takes in a list of clubs, of type "Club"
        rewrites the club file with all clubs in the list'''
        
        self.club_files.write_club(clubs)
        return


    def get_all_tournaments(self):
        '''Returns a list of all tournaments in tournament file,
        tournaments are of type "Tournament"'''
        
        return self.tournament_files.read_tournament()

    def add_tournament(self, tournament: Tournament):
        '''Takes in a tournament, of type "Tournament",
        adds the tournament to the bottom of the tournament file'''
        
        self.tournament_files.add_tournament(tournament)
        return

    def write_tournament(self, tournaments: list):
        '''Takes in a list of tournaments, of type "Tournament",
        rewrites the tournament file with all tournaments in the list'''
        
        self.tournament_files.write_tournament(tournaments)
        return

