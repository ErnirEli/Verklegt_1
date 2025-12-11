from Datalayer.data_api import DataAPI
from datetime import datetime
from Error.tournament_error import *
from datetime import *
from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

class ValidateTournament:
    def __init__(self):
            self._data = DataAPI()
    


    def validate_name(self, name: str):
        if name.lower() == "q":
             raise BackButton
        if not name:
            raise EmptyInput
        
        return True


    def validate_start_date_and_end_date(self, start_date:str, end_date:str):
        if start_date.lower() == "q" or end_date.lower() == "q":
             raise BackButton
        
        if not start_date or not end_date:
            raise EmptyInput
        
        if start_date.count("-") != 2 or end_date.count("-") != 2:
             raise InvalidFormat    
        
    
        start_date = start_date.split("-")
        end_date =  end_date.split("-")
         
        try:
             start_date = date(int(start_date[2]), int(start_date[1]), int(start_date[0]))
        except ValueError:
            raise DateDoesNotExistError
        try:
            end_date = date(int(end_date[2]), int(end_date[1]), int(end_date[0]))
        except ValueError:
             raise DateDoesNotExistError 


        if start_date > end_date:
           raise InvalidStartDateBefore
        
        today = datetime.today().date()
        if start_date < today:
            raise InvalidStartDateInPast
        
        days = (end_date - start_date).days
        if days < 2 or days > 7:
             raise InvalidAmountOfDays
    
        return True


                

    def validate_venue(self, venue: str):
        if venue.lower() == "q":
             raise BackButton
        if not venue:
            raise EmptyInput
        return True
    
    def validate_contract(self, contract: str):
        if contract.lower()  == "q":
             raise BackButton
        if not contract:
            raise EmptyInput
        return True
    
    def validate_contact_email(self, email: str):
        if email.lower() == "q":
             raise BackButton        
        if not email:
            raise EmptyInput
        if "." not in email or "@" not in email:
            raise InvalidContactEmail
        return True
        
    def validate_contact_numer(self, number: str):
        if number.lower() == "q":
             raise BackButton
        if not number:
                return EmptyInput
        if not number.isnumeric() or len(number) != 10:
                raise InvalidContactNumber
        
        return True

    def validate_number_of_teams(self, num_of_teams: str):
        if num_of_teams.lower() == "q":
             raise BackButton
        
        num_of_teams = int(num_of_teams)
        
        if num_of_teams < 16 or num_of_teams > 64:
            raise WrongNumOfTeams
        
        return True
    def validate_teams_in_tournament(self, team_to_tournament: str, teams_in_tournament: list):
        if team_to_tournament.lower() == "q":
             raise BackButton
        
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
        if id.lower() == "q":
             raise BackButton
        
        if not id:
             raise EmptyInput
        
        all_tournaments = self._data.get_all_tournaments()
        for i in all_tournaments:
             if i.id == id:
                  raise IdAlreadyExists
        return True
    
    def validate_servers(self, servers: str, num_of_teams: int):
        if servers.lower() == "q":
             raise BackButton
        
        servers = int(servers)

        if num_of_teams < 32:
             if servers < 2 or servers > 4:
                  raise InvalidServers
        if num_of_teams >= 32:
            if servers < 4 or servers > 7:
                raise InvalidAmountOfDays
       
        return True
        