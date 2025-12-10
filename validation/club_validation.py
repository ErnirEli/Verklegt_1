from Datalayer.data_api import DataAPI
from Error.club_error import *

class ValidateClub:
    def __init__(self):
        self._data = DataAPI()

    def name_validation(self, name: str):
        if not name:
            raise EmtptyInput
        
        club_list = self._data.get_all_clubs()


        for club in club_list:
            if name.strip() == club.name:
                raise ClubNameExistsError
            
        return True

    def validate_colors(self, color: str): #colors string eða list?
        if not color:
            raise EmtptyInput
        
        color_list = ["blue", "light blue", "red", "light red", "orange", "green", "light green", "yellow", "black", "white", "brown", "purple", "light purple", "cyan", "light cyan", "light gray", "dark gray"]      
        
        if color.strip().lower() not in color_list:
            raise ColorNotAvailable

        return True

    def validate_hometown(self, hometown: str):
        if not hometown:
            raise EmtptyInput
        return True


    def validate_country(self, country: str):
        if not country:
            raise EmtptyInput
        
        return True
    
    def validate_num_of_teams(self, num_of_teams):
        int(num_of_teams)
        if num_of_teams > 10 or num_of_teams < 1:
            raise InvalidNumOfTeams
        
        return True
  
        
    def validate_teams_in_club(self, team_to_club, teams_in_club):
        all_teams = self._data.get_all_teams()
        all_team_names = []
        
        
        for team in all_teams:
            all_team_names.append(team.name)
            if team.name == team_to_club:
                raise TeamNotAvailableError
         
        
        if team_to_club in teams_in_club:
            raise TeamAlreadyInClubError
        if team_to_club not in all_team_names:
            raise TeamDoesNotExistError
        
        return True