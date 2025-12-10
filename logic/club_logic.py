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

    def create_club(self, name: str, colors: str, hometown: str, country: str, team_list: list) -> None:
        '''Creates a instance of Club and saves it'''
        club: Club = Club(name, colors, hometown, country)

        self._data_api.add_club(club)
        return 
    
    def add_teams(self, team_list: list, club: Club) -> None:
        '''Adds all teams to a club'''

        teams = self._data_api.get_all_teams()

        for team in teams:
            team: Team

            if team.name in team_list:
                team.club = club.name

        self._data_api.write_teams(team)

    def get_club_teams(self, club: Club):
        '''Gets all teams that are a part of a club'''

        club_teams = []

        teams = self._data_api.get_all_teams()

        for team in teams:
            team: Team

            if team.club == club.name:
                club_teams.append(club.name)

        return club_teams

    def add_team(self, club: Club, new_team: Team):
        '''Adds a single team to a club'''
        
        new_team.club = club.name
        return new_team
    
    def remove_team(self, unwanted_team: Team):
        '''removes a team from a club'''

        unwanted_team.club = "None"
        return unwanted_team
    
    def club_info(self, club: Club):

        club_teams = self.get_club_teams(club)
        
        return (
            f"name: {club.name} \n"
            f"colors{club.colors} \n"
            f"Hometown: {club.hometown}\n"
            f"Country: {club.country}"
        )