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
from data.data_api import DataAPI
from models.tournament import Tournament
from logic.tournament_logic import Team


class TournamentLogic:
    
    _data_api: DataAPI
    
    def __init__(self, data_api: DAtaAPI) -> None:
        self._data_api.read_all_Tournaments

    def list_all_tournaments(self)-> List[Tournament]:
        return self._data_api.read_all_Tournaments

    def create_tournaments(self, start_date: str, end_date: str, name: str, venue: str, contract: str, contact_person_email:str, contact_person_number:str, team_list: list) -> Tournament:     
        tournament: Tournament = Tournament(start_date, end_date, name, venue, contract, contact_person_email, contact_person_number, team_list)
        self._data_api.save_tournament(tournament)
        return tournament


    def add_team(self, team: Team, tournament: Tournament):
        tournament.teams.append(team)
        self._data_api.save_tournament(tournament)
        return tournament
    
    def tournament_schedule(self, tournament: Tournament, star_date: str, end_date: str):
        #torunament name    start date      end date


        return
    
    def tournament_results(self):
        return
    
    def tournament_bracket(self):
        return