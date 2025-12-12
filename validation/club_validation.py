from Datalayer.data_api import DataAPI
from Error.club_error import *
from models.team import Team
from Error.general_error import EmptyInput, BackButton
from models.club import Club

class ValidateClub:
    def __init__(self):
        self._data = DataAPI()

    def name_validation(self, name: str):
        if name.lower() == "q":
            raise BackButton
        
        if not name:
            raise EmptyInput
        
        club_list = self._data.get_all_clubs()


        for club in club_list:
            if name.strip() == club.name:
                raise ClubNameExistsError
            
        return True

    def validate_colors(self, color: str): #colors string eða list?
        if color.lower() == "q":
            raise BackButton
        if not color:
            raise EmptyInput
        
        color_list = ["blue", "light blue", "red", "light red", "orange", "green", "light green", "yellow", "black", "white", "brown", "purple", "light purple", "cyan", "light cyan", "light gray", "dark gray"]      
        
        if color.strip().lower() not in color_list:
            raise ColorNotAvailable

        return True

    def validate_hometown(self, hometown: str):
        if hometown.lower() == "q":
            raise BackButton
        if not hometown:
            raise EmptyInput
        return True


    def validate_country(self, country: str):
        if country.lower() == "q":
            raise BackButton
        if not country:
            raise EmptyInput
        
        return True
    
    def validate_num_of_teams(self, num_of_teams: str):
        if num_of_teams.lower() == "q":
            raise BackButton
        num_of_teams = int(num_of_teams)
        if num_of_teams > 5 or num_of_teams < 1:
            raise InvalidNumOfTeams
        
        return True

    
    def validate_teams_in_club(self, team_to_club: str, teams_in_club: list = []):
        if team_to_club.lower() == "q":
            raise BackButton
        all_teams = self._data.get_all_teams()
    
        for team in all_teams:
            team: Team

            if team.name == team_to_club:
                break
        else:
            raise TeamDoesNotExistError
        
        if team.club != "None":
            raise TeamNotAvailableError
        
        if team_to_club in teams_in_club:
            raise TeamAlreadyInClubError

        
        return True
    
    def does_club_exist(self, club_name: str):
        all_clubs: list[Club] = self._data.get_all_clubs()
        for club in all_clubs:
            if club.name == club_name:
                return True
        
        raise ClubDoesNotExist
    
    def validate_club_to_remove(self, team_name: str):
        all_teams = self._data.get_all_teams()
        for team in all_teams:
            team: Team
            if team.name == team_name:
                break
        else: 
            raise TeamDoesNotExistError
        
        return True
