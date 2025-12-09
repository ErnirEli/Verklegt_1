from Datalayer.data_api import DataAPI
from datetime import datetime
from Error.tournament_error import *
class ValidateTournament:
    def __init__(self):
            self._data = DataAPI()
    


    def validate_name(self, name: str):
        if not name:
            raise EmptyInput
        return True

    def validate_start_date_and_end_date(self, start_date:int, end_date:int):
        if not start_date or not end_date:
            raise EmptyInput
            
        
        start_date_checker:datetime = datetime.strptime(start_date, "%d.%m.%y")
        end_date_checker: datetime = datetime.strptime(end_date, "%d.%m.%y")
        if start_date_checker >= end_date_checker:
           raise InvalidStartDateBefore
        
    
        today = datetime.today()
        if start_date_checker > today:
            raise InvalidStartDateInPast
                
        return True


    def validate_venue(self, venue: str):
        if not venue:
            raise EmptyInput
        return True
    
    def validate_contract(self, contract: str):
        if not contract:
            raise EmptyInput
        return True
    
    def validate_contact_email(self, email: str):
        if not email:
            raise EmptyInput
        if "." and "@" in email and not isinstance(email, str):
                raise InvalidContactEmail
        
        return True
        
    def validate_contact_numer(self, number: str):
        if not number:
                return EmptyInput
        if not number.isnumeric() and len(number) != 10:
                raise InvalidContactNumber
        
        return True

    def validate_number_of_teams(self, num_of_teams: str):
        

        if len(num_of_teams) < 16 and len(num_of_teams) > 64:
            raise WrongNumOfTeams
        
        return True
    def validate_teams_in_tournament(self, team_to_tournament: str, teams_in_tournament: list):
        
        team_names = []
        all_teams = self._data.get_all_teams()

        for team in all_teams:
            team_names.append(team.name)

        if team_to_tournament not in team_names:
            raise TeamDoesNotExist
        
        
        if team_to_tournament in teams_in_tournament:
            raise TeamAlreadyInTournament
        
        return True
    

    def validate_id(self, id: str):
        if not id:
             raise EmptyInput
        
        all_tournaments = self._data.get_all_tournaments()
        for i in all_tournaments:
             if i.id == id:
                  raise IdAlreadyExists
        return True
    
    def validate_servers(self, servers: str):
        int(servers)
        if servers > 9 and servers < 1:
             raise InvalidServers
        return True
        