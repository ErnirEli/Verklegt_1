from data.data_api import DataAPI
from datetime import datetime

class ValidateTournament:
    def __init__(self):
            pass
    
    def validate_start_date_and_end_date(self, start_date:int, end_date:int):
        if not start_date or not end_date:
            return (False, "Tournament needs to have a start date and an end date")
        
        start_date_checker:datetime = datetime.strptime(start_date, "%d.%m.%y")
        end_date_checker: datetime = datetime.strptime(end_date, "%d.%m.%y")
        if start_date_checker >= end_date_checker:
            return (False, "Start date needs to be before the end date")

        today = datetime.today()
        if start_date_checker > today:
                return (False, "The start date is in the past")

        return True,

    def validate_name(self, name: str):
        if not name:
            return (False, "Tournament needs to have a name")

    def validate_venue(self, venue: str):
        if not venue:
            return (False, "Tournament needs a venue")
    
    def validate_contract(self, contract: str):
        if not contract:
            return (False, "Tournament needs a contract")
    
    def validate_contact_person(self, email: str, number: str):
        if not email:
            return (False, "Tournament needs a contact persons email)")
        if "." and "@" in email and not isinstance(email, str):
                return (False, "email is not valid")
        if not number:
                return (False, "Tournament neeeds a contact persons phone number")
        if not number.isnumeric()and len(number) != 7:
                return (False, "Phone number is not valid")
        
        return True,

    def validate_number_of_teams(self):
        team_list: list = DataAPI.get_all_teams
               
        if len[team_list] < 16:
            return (False, "Tournament needs to have at least 16 teams")
        return True,