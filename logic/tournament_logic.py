#Requirements:
# Organizer creates the tournaments
# Stored inof on tournaaments: 
# start date, 
# end date,
# unique name,
# venue
# contract,
# contact person (email or phone)

# Anyone can view tournaments per team
# anyone can viwe tournaments per player

from typing import List
from datetime import datetime
from data.data_api import DataAPI
from models.tournament import Tournament
from models.exceptions import ValidationError
from logic.tournament_logic import Team
from datetime import datetime


class TournamentLogic:
    def __init__(self) -> None:
        self._data_api.read_all_Tournaments

    def list_all_tournaments(self)-> List[Tournament]:
        return self._data_api.read_all_Tournaments

    def create_tournaments(self, start_date: int, end_date: int, name: str, venue: str, contract: str, contact_person: tuple, team_list: list) -> Tournament:
        start_date_checker:datetime = datetime.strptime(start_date, "%d.%m.%y")
        end_date_checker: datetime = datetime.strptime(end_date, "%d.%m.%y")
        self._validate_tournament(start_date_checker, end_date_checker, name, venue,contract, contact_person, team_list)
        tournament: Tournament = Tournament(start_date, end_date, name, venue, contract, contact_person)
        self._data_api.save_tournament(tournament)
        return tournament

    def _validate_tournament(self,start_date: datetime, end_date: datetime, name: str, venue: str, contract: str, contact_person:tuple, team_list: list ):
        if not start_date or not end_date:
            raise ValidationError("Tournament needs to have a start date and an end date")
        if not name:
            raise ValidationError("Tournament needs to have a name")
        if start_date >= end_date:
            raise ValidationError("Start date needs to be before the end date")
        if not venue:
            raise  ValidationError("Tournament needs a venue")
        if not contract:
            raise ValidationError("Tournament needs a contract")
        if not contact_person:
            raise ValidationError("Tournament needs a contact person)")
        if len[team_list] < 16:
            raise ValidationError("Tournament needs to have at least 16 teams")
        
    # def tournament_teams(self,):
    #     tournament_list = []
    #     tournament_list.append()


    def add_team(self, team: List[Team], tournament: List[Tournament]):
        tournament.append(team)
        self._data_api.save_tournament(tournament)
        return tournament
    
    def tournament_schedule(self):
        return
    
    def tournament_results(self):
        return
    
    def tournament_bracket(self):
        return