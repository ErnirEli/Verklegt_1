from Datalayer.data_api import DataAPI
from models.tournament import Tournament
from logic.schedule_logic import Schedule
from models.team import Team
from models.match import Match
from datetime import date
from datetime import time
import random

class TournamentLogic:
    
    def __init__(self) -> None:
        self._data_api = DataAPI()

    def list_all_tournaments(self)-> list:
        return self._data_api.get_all_tournaments()

    def add_teams(self, teams: list, tournament: Tournament) -> Team:
        for team in teams:
            if team.tour_IDs == 'None':
                team.tour_IDs = tournament.name

            else:
                team.tour_IDs += f" {tournament}"

        return team
        
    def tournament_schedule(self):
        #torunament name    start date      end date
        tournaments = self.get_all_tournaments()
        return tournaments


    
    def tournament_results(self, ):
        
        return
    
    def create_a_tournament(self, tournament_id: str, name: str, venue: str, start_date: str,
                end_date: str, contact: str, contact_email:str,
                contact_number:str, servers: int):
        
        new_tournament = Tournament(tournament_id, name, venue, start_date, end_date,
                                    contact, contact_email, contact_number, servers)
        self._data_api.add_tournament(new_tournament)
        return
    
    def tournament_bracket(self):
        return
    

    def create_tournament_schedule(self) -> list:
        tournaments = self._data_api.get_all_tournaments()
        tournament = tournaments[0]

        tournament_schedule = Schedule(tournament)

        tournament_schedule.create_playoffs()
        tournament_schedule.create_rounds()
        
        