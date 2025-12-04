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


    def __init__(self, data_api: DataAPI) -> None:
        self._data_api = data_api
    
    def list_all_teams(self) -> List[Team]:
        """Returns a list of all teams"""
        return self._data_api.get_all_teams()


    def create_team(self, name: str, captain: str, web_link: str = None, ASCII: str = None) -> Team:
        team: Team = Team(name, captain, web_link, ASCII)
        self._data_api.add_team(team)
        return team
        

    
    def add_player(self, team: Team, new_player: Player):
        team.players.append(new_player)
        self._data_api.add_team(team)
        return team
    
    def remove_player(self, team: Team, unwanted_player: Player):
        team.players.remove(unwanted_player)
        self._data_api.add_team(team)
        return team
    
    def team_stats(self):
        #Tournaments won, second and third
        #Tournemnts played in
        
        
        return
    
    def team_info(self, team: Team):
        return {
            "name": team.name,
            "Captain": team.captain,
            "Players": team.players,
            "Web link": team.web_link,
            "ASCIIlogo": team.ASCII
        }
        
    