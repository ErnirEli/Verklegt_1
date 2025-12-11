# requirements:
# clubs, players, teams get rewards (points) for winning
from typing import List
from Datalayer.data_api import DataAPI
from models.club import Club
from models.team import Team


class ClubLogic:
    def __init__(self) -> None:
        self._data_api = DataAPI()
    
    
    def list_all_clubs(self) -> List[Club]:
        '''Takes in nothing and returns a list of all existing clubs of type Club'''

        return self._data_api.get_all_clubs()

    def create_club(self, name: str, color: str, hometown: str, country: str, team_list: list[str]) -> None:
        '''Takes in a name, color, hometown, country all of type string, also takes in a list of team names, of type string.
        Creates a club of type "Club" and adds all teams from list to the club. Returns None.
        Only runs after all validation checks are valid.'''

        club: Club = Club(name, color, hometown, country)


        self.add_teams(team_list, club)
        self._data_api.add_club(club)
        return 
    
    def add_teams(self, team_list: list[str], club: Club) -> None:
        '''Takes in a list of team names of type string and a club of type "Club".
        adds all teams in the list to the club.
        Runs automatically when a club is created'''

        teams: list[Team] = self._data_api.get_all_teams()

        for team in teams:
            # Check if team is supposed to go in club
            if team.name in team_list:
                team.club = club.name

        self._data_api.write_teams(teams)

    def get_club_teams(self, club: Club) -> list[Team]:
        '''Takes in a club of type Club and returns a list of all teams in the club, of type "Team".
        Only runs after all validation checks are Valid'''

        club_teams: list[Team] = []
        teams: list[Team] = self._data_api.get_all_teams()

        for team in teams:
            if team.club == club.name:
                club_teams.append(club.name)

        return club_teams

    def add_team(self, club: Club, new_team: Team) -> None:
        '''Takes in a club, og type "Club" and a team of type Team.
        adds team tou the club.
        Only runs after all validation checks are valid'''
        
        teams: list[Team] = self._data_api.get_all_teams()

        for team in teams:
            if team.name == new_team.name:
                new_team.club = club.name
                team.club = club.name
                break
        return
    
    def remove_team(self, unwanted_team: Team) -> None:
        '''Takes in a team of type "Team" and removes it from club.
        Only runs after ale validation checks are valid.'''

        teams: list[Team] = self._data_api.get_all_teams()

        for team in teams:
            if team.name == unwanted_team.name:
                unwanted_team.club = "None"
                team.club = "None"
                break
        return
    
    def get_club(self, club_name: str) -> Club:
        '''Takes in club name of type string and returns club of type Club.
        Only runs after ale validation checks are valid.'''

        clubs: list[Club] = self._data_api.get_all_clubs()

        for club in clubs:
            if club.name == club_name:
                return club
            
        return
    
    def club_info(self, club: Club):

        club_teams = self.get_club_teams(club)
        return (
            f"name: {club.name} \n"
            f"color{club.color} \n"
            f"Hometown: {club.hometown}\n"
            f"Country: {club.country}"
        )