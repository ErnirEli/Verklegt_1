from Datalayer.data_api import DataAPI
from models.club import Club
from models.team import Team
from typing import List


class ClubLogic:
    def __init__(self) -> None:
        self._data_api = DataAPI()
    
    
    def list_all_clubs(self):
        '''returns a list of all teams'''
        return self._data_api.get_all_clubs()

    def create_club(self, name: str, color: str, hometown: str, country: str, num_of_teams: str, teams_in_club: List[Team]) -> Club:
        
        for team in teams_in_club:
            team.club = name

        club: Club = Club(name, color, hometown, country)
        self._data_api.add_club(club)
        return club
    
    def add_team(self, club: Club, new_team: Team):
        new_team.club = club.name
        return new_team
    
    def remove_team(self, unwanted_team: Team):
        unwanted_team.club = None
        return unwanted_team
    
    def club_info(self, club: Club):
        teams = DataAPI().get_all_teams()
        club_teams = []
        for team in teams:
            if team.club == club.name:
                club_teams.append(club.name)
        
        return (
            f"name: {club.name} \n"
            f"color{club.color} \n"
            f"Hometown: {club.hometown}\n"
            f"Country: {club.country}"
            f"Teams in club: {club_teams}"
        )