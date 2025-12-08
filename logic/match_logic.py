# Requirements:
# games get created automatically
# Organizer inputs match results
# System uptades schedule after results


from typing import List
from Datalayer.data_api import DataAPI
from models.match import Match




class MatchLogic:

    _data_api: DataAPI

    def __init__(self, data_api: DataAPI) -> None:
        self._data_api = data_api

    def list_all_matches(self)-> List[Match]:
        return

        
    def create_match(self, tournament_teams: list)-> Match:
        
        return 
    

    def game_results(self):
        return
    
    def get_game(self):
        return