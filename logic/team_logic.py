from typing import List
from Datalayer.data_api import DataAPI 
from models.team import Team
from models.player import Player


# Requirements:
# Sama lið bara búið til 1 sinni.
# Organizer can register new teams
# team data: name, captain, link to web page, ASCII logo.
# captains add and or change players info



class TeamLogic:
    _data_api: DataAPI


    def __init__(self) -> None:
        self._data_api = DataAPI()
    
    def list_all_teams(self) -> List[Team]:
        """Returns a list of all teams"""
        return self._data_api.get_all_teams()


    def create_team(self, name: str, captain: str, web_link: str = None, ASCII: str = None) -> Team:
        '''creaetes a team only if all validation condition have been met'''
        team: Team = Team(name, captain, web_link, ASCII)
        self._data_api.add_team(team)
        return team
        

    
    def add_player(self, team: Team, new_player: Player):
        '''Adds a selected player to selected team'''
        new_player.team_name = team.name
        return new_player
    
    

    def remove_player(self, unwanted_player: Player):
        '''Removes a selected player out of selected team'''
        unwanted_player.team_name = None
        return unwanted_player
    

    def team_info(self, team: Team):
        '''Gives all info on team'''
        players = DataAPI().get_all_players()
        team_players = []
        for player in players:
            if player.team_name == team.name:
                team_players.append(player.handle)
        
        return (
            f"name: {team.name} \n"
            f"Captain: {team.captain} \n"
            f"Club: {team.club}"
            f"Players: {team_players} \n"
            f"Web link: {team.web_link} \n"
            f"ASCIIlogo: {team.ASCII} \n"
            f"Tournaments played in: {team.tournament} \n"
            f"Tournaments won: {team.wins}")