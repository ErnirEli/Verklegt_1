from typing import List
from logic.team_logic import TeamLogic
from models.team import Team
from data.data_api import DataAPI

class logicAPI:

    def __init__(self) -> None:
        data_api: DataAPI = DataAPI()
        self._team_logic = TeamLogic(data_api)

    def list_teams(self) -> list[Team]:
        return self._team_logic.list_all_teams()
    
    def create_team(self,name: str, captain: str, web_link: str, ASCII = str) -> Team:
        return self._team_logic.create_team(name, captain, web_link, ASCII )