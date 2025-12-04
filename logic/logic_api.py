from typing import List
from logic.team_logic import TeamLogic
from models.team import Team
from data.data_api import DataAPI
from logic.tournament_logic import TournamentLogic
from logic.match_logic import MatchLogic
from models.tournament  import Tournament
from models.match import Match


class logicAPI:

    def __init__(self) -> None:
        data_api: DataAPI = DataAPI()
        self._team_logic = TeamLogic(data_api)
        self._tournament_logic = TournamentLogic(data_api)
        self._match_logic = MatchLogic(data_api)
#Teams
    def list_teams(self) -> list[Team]:
        return self._team_logic.list_all_teams()
    
    def create_team(self,name: str, captain: str, web_link: str, ASCII = str) -> Team:
        return self._team_logic.create_team(name, captain, web_link, ASCII )

#Tournaments

    def list_tournaments(self) -> None:
        return self.tournament_logic.list_all_tournaments()
    
    def create_tournament(self, start_date: int, end_date: int, name: str, venue: str, contract: str, contact_person: tuple, team_list: list) -> List[Tournament]:
        return self._tournament_logic.create_tournaments(start_date, end_date, name, venue, contract, contact_person, team_list)
#Matches
    
    def list_matches(self) -> None:
        return self._match_logic.list_all_matches()
    def create_match(self,teams: tuple):
        return self._match_logic.create_match(teams)
