from typing import List
from data.data_api import DataAPI 
from models.team import Team
from models.exceptions import ValidationError
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
        return self._data_api.read_all_teams()


    def create_team(self, name: str, captain: str, team_list: list, web_link: str = None, ASCII: str = None) -> Team:
        if not name:
            raise ValidationError("Team needs to have a name")
        if not captain:
            raise ValidationError("Team needs to have a captain")
        if name.strip() in team_list:
            raise ValidationError("Team already exists")
        if not isinstance(captain, str):
            raise ValidationError("Can't have more than one captain")
        team: Team = Team(name, captain, web_link, ASCII)
        self._data_api.save_team(team)
        return team
        

    
    def add_player(self, team: Team, new_player: Player):
        team.players.append(new_player)
        self._data_api.save_team(team)
        return team
    
    def remove_player(self, team: Team, unwanted_player: Player):
        team.players.remove(unwanted_player)
        self._data_api.save_team(team)
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
            "Weblink": team.web_link,
            "ASCIIlogo": team.ASCII
        }
        
    