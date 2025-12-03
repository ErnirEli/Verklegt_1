from typing import List
from data.data_api import DataAPI 
from models.team import Team
from models.exceptions import ValidationError


# Requirements:
# Sama lið bara búið til 1 sinni.
# Organizer can register new teams
# team data: name, captain, link to web page, ASCII logo.
# captains add and or change players info
class Team:
    def __init__(self):
        pass


class TeamLogic:
    _data_api: DataAPI


    def __init__(self, data_api: DataAPI) -> None:
        self._data_api = data_api
    
    def list_all_teams(self) -> List[Team]:
        """Returns a list of all teams"""
        return self._data_api.read_all_teams()


    def create_team(self, name: str, captain: str, web_link: str = None, ASCII: str = None ) -> Team:
        if not name:
            raise ValidationError("Team needs to have a name")
        if not captain:
            raise ValidationError("Team needs to have a captain")
        if name.strip() in team_list:
            raise ValidationError("Team already exists")
        if captain != str:
            raise ValidationError("Can't have more than one captain")
        team: Team = Team(name, captain, web_link, ASCII)
        self._data_api.save_team(team)
        return team
        

    
    def add_player(self, team: List[Team], new_player: List[Player]):
        team.append(new_player)
        self._data_api.save_team(team)
        return team
    
    def remove_player(self, team: List[Team], unwanted_player: List[Player]):
        team.remove(unwanted_player)
        self._data_api.save_team(team)
        return team
    
    def team_stats(self):
        return
    
    def team_info(self):
        return