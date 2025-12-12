from typing import List
from Datalayer.data_api import DataAPI 
from models.team import Team
from models.player import Player
from typing import List

# Requirements:
# Sama lið bara búið til 1 sinni.
# Organizer can register new teams
# team data: name, captain, link to web page, ASCII logo.
# captains add and or change players info



class TeamLogic:

    def __init__(self) -> None:
        self._data_api = DataAPI()
    
    def list_all_teams(self) -> List[Team]:
        '''Takes in nothing and returns a list of all existing teams of type Team'''

        return self._data_api.get_all_teams()

    def create_team(self, name: str, captain: str, web_link: str, ASCII: str, team_players: list[str]) -> Team:
        '''Takes in a name, captain handle, web link, ASCII all of string type,
        also takes in a list of player handles of type string. 
        Creates a team and adds players to the team.
        Returns the team of type Team.
        Only runs after all validation checks are valid.'''

        team: Team = Team(name, captain, web_link = web_link, ASCII = ASCII)

        # Adds team name to player
        self.add_players(team, team_players)


        self._data_api.add_team(team)

        return team
        
    def add_players(self, team: Team, new_players: list[str]):
        '''Takes in a team of type Team, 
        a list of player handles of type string,
        adds all players to the team. 
        Only runs when a team is created and 
        after all validation checks are valid'''

        players = self._data_api.get_all_players()

        # Finds player with the right handle and adds team name to the player
        for player in players:
            if player.handle in new_players:
                player: Player

                player.team_name = team.name

        
        self._data_api.write_players(players)

        return 
    
    def add_player(self, team: Team, wanted_player: Player) -> None:
        '''Takes in a team, of type Team,
        and a player of type Player,
        and adds the player to the team.
        Only runs after all validation checks are valid.'''

        players: list[Player] = self._data_api.get_all_players()

        for player in players:
            if player.handle == wanted_player.handle:
                player.team_name = team.name
    
        self._data_api.write_players(players)
        return
    
    def remove_player(self, unwanted_player: Player) -> None:
        '''Takes in a player, of type Player, 
        and removes him from team'''

        players: list[Player] = self._data_api.get_all_players()

        for player in players:
            if player.handle == unwanted_player.handle:
                player.team_name = "None"

        self._data_api.write_players(players)
        return 
    
    def get_team_players(self, team_name: str) -> list[Player]:
        '''Takes in a team name of type string, returns a list of all players in the team, of type Player'''

        players: list[Player] = self._data_api.get_all_players()
        team_players: list[Player] = []

        for player in players:
            if player.team_name == team_name:
                team_players.append(player)

        return team_players

    def get_team(self, name: str) -> Team:
        '''Takes in a team name as a string,
        finds the team with the right name and
        returns it of type Team'''

        teams: list[Team] = self._data_api.get_all_teams()

        for team in teams:
            if team.name == name:
                return team
    
