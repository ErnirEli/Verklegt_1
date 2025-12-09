# requirements:
# Name
# age
# home adress
# email
# link
# handle
# team
from models.player import Player
from Datalayer.data_api import DataAPI
from Error.player_error import *
from datetime import *

class ValidatePlayer:



    def __init__(self):
        self._data = DataAPI()
    

    
    def validate_name(self, name:str):
        if not name or name.strip() == "":
            raise EmptyInput                    # We raise the EmptyInput Exception class only when nothing is input
        
        return True
    
    def validate_age(self, dob: str):
        if not dob:
            raise EmptyInput 
                    
        if "/" not in dob:
            raise InvalidAgeException
        
        
        dob = dob.split("/")
        dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
        today = datetime.today().date()
        age = today - dob
        age = (age/365.25).days
        if age < 18:
            raise TooYoungError
        if age > 99:
            raise TooOldError
        
        return True




    def validate_home_adress(self, adress: str):
        if not adress or adress.strip() == "":
            raise EmptyInput
        return True

    def validate_email(self, email: str):
        if not email or email.strip() == "":
            raise EmptyInput
        if "@" not in email or "." not in email:
            raise InvalidEmailException
        return True

    def validate_number(self, number: str):
        if number == "354":
            raise EmptyInput
        if not number.isnumeric() or len(number) != 10:
            raise invalidNumberException
        return True

    def validate_link(self, link: str):
        if link.strip() == "https://":
            raise EmptyInput
        if "." not in link:
            raise InvaldlinkException
        return True
        #eitthvað fleira??

    def validate_handle(self, handle: str):
        if not handle or handle.strip() == "":
            raise EmptyInput
        players = self._data.get_all_players()
        if "," in handle or "/" in handle:
            raise InvalidCharacterHandle
        for line in players:
            if line.handle == handle:
                raise HandleExistsException
        return True
            
