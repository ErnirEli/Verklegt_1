from Datalayer.data_api import DataAPI
from Error.club_error import *
from models.team import Team
from Error.general_error import EmptyInput

class ValidateClub:
    def __init__(self):
        self._data = DataAPI()

    def name_validation(self, name: str):
        if not name:
            raise EmptyInput
        
        club_list = self._data.get_all_clubs()


        for club in club_list:
            if name.strip() == club.name:
                raise ClubNameExistsError
            
        return True

    def validate_colors(self, color: str): #colors string eða list?
        if not color:
            raise EmptyInput
        
        color_list = ["blue", "light blue", "red", "light red", "orange", "green", "light green", "yellow", "black", "white", "brown", "purple", "light purple", "cyan", "light cyan", "light gray", "dark gray"]      
        
        if color.strip().lower() not in color_list:
            raise ColorNotAvailable

        return True

    def validate_hometown(self, hometown: str):
        if not hometown:
            raise EmptyInput
        return True


    def validate_country(self, country: str):
        if not country:
            raise EmptyInput
        
        return True
    
    def validate_num_of_teams(self, num_of_teams):
        num_of_teams = int(num_of_teams)
        if num_of_teams > 10 or num_of_teams < 1:
            raise InvalidNumOfTeams
        
        return True

        
    def validate_teams_in_club(self, team_to_club: str, teams_in_club: list):
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