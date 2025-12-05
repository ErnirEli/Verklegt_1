# requirements:
# clubs, players, teams get rewards (points) for winning
from typing import List
from Datalayer.data_api import DataAPI
from models.club import Club
from models.team import Team


class ClubLogic:
    def __init__(self, data_api: DataAPI) -> None:
        self._data_api = data_api
    
    
    def list_all_clubs(self) -> List[Club]:
        '''returns a list of all teams'''
        return self._data_api.gett_all_clubs

    def create_club(self, name: str, colors: str, hometown: str, country: str) -> Club:
        club: Club = Club(name, colors, hometown, country)
        self._data_api.add_club
        return club
    
    def add_team(self, club: Club, new_team: Team):
        new_team.club_name = club.name
        return new_team
    
    def remove_team(self, unwanted_team):
        unwanted_team.club_name = None
        return unwanted_team
    
    def club_info(self, club: Club):
        teams = DataAPI().get_all_teams()
        club_teams = []
        for team in teams:
            if team.club_name == club.name:
                club_teams.append(club.name)
        
        return (
            f"name: {club.name} \n"
            f"colors{club.colors} \n"
            f"Hometown: {club.hometown}\n"
            f"Country: {club.country}"
        )