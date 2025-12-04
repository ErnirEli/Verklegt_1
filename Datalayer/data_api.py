from Datalayer.player_data import PlayerFiles
from Datalayer.team_data import TeamFiles
from Datalayer.temporary import Player
from Datalayer.temporary import Team
lksadj
class DataAPI():
    def __init__(self):
        self.player_files: PlayerFiles = PlayerFiles()
        self.team_files: TeamFiles = TeamFiles()

    def get_all_players(self):
        '''Returns a list of all players, players are of type Player'''
        return self.player_files.read_player()
    
    def add_player(self, player: Player):
        '''Adds a new player to the bottom of the file'''
        self.player_files.add_player(player)

    def rewrite_players(self, players: list):
        '''Rewrites the whole file with all exiting players'''
        self.player_files.write_player(players)

    def get_all_teams(self):
        '''Returns a list of all tems, teams are of type Team'''
        return self.team_files.read_team()

    def add_team(self, team: Team):
        '''Adds a new team to the bottom of the file'''
        self.team_files.add_team(team)

    def rewrite_teams(self, teams: list):
        '''Rewrites the whole file with all existing teams'''
        self.team_files.write_team(teams)