# requirements:
# Name
# age
# home adress
# email
# link
# handle
# team

from Datalayer.data_api import DataAPI
from Error.player_error import *
from datetime import date, datetime
from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

class ValidatePlayer:



    def __init__(self):
        self._data = DataAPI()
    

    
    def validate_name(self, name:str):
        if name.lower() == "q":
            raise BackButton
        if not name or name.strip() == "":
            raise EmptyInput                    # We raise the EmptyInput Exception class only when nothing is input

        return True
    
    def validate_age(self, dob: str):
        if dob.lower() == "q":
            raise BackButton
        
        if not dob:
            raise EmptyInput 
                    
        if dob.count("-") != 2:
            raise InvalidAgeException
        
        dob = dob.split("-")
        try:
            dob = date(int(dob[2]), int(dob[1]), int(dob[0]))
        except ValueError:
            raise DateDoesNotExistError

        today = datetime.today().date()
        age = today - dob
        age = (age/365.25).days
        if age < 18:
            raise TooYoungError
        if age > 99:
            raise TooOldError
        
        return True




    def validate_home_adress(self, address: str):
        if address.lower() == "q":
            raise BackButton
        if not address:
            raise EmptyInput
        
        
        return True
    

    def validate_email(self, email: str):
        if email.lower() == "q":
            raise BackButton
        if not email or email.strip() == "":
            raise EmptyInput
        if "@" not in email or "." not in email:
            raise InvalidEmailException

        return True

    def validate_number(self, number: str):
        if number.lower() == "q":
            raise BackButton
        if number == "354":
            raise EmptyInput
        if not number.isnumeric() or len(number) != 10:
            raise invalidNumberException
        return True

    def validate_link(self, link: str):
        if link.lower() == "q":
            raise BackButton
        if link.strip() == "https://":
            raise EmptyInput
        if "." not in link:
            raise InvaldlinkException
        return True
    
        #eitthvað fleira??

    def validate_handle(self, handle: str):
        if handle.lower() == "q":
            raise BackButton    
        if not handle or handle.strip() == "":
            raise EmptyInput
        
        players = self._data.get_all_players()
        if "," in handle or "/" in handle:
            raise InvalidCharacterHandle
        for line in players:
            if line.handle == handle:
                raise HandleExistsException
        return True
            
    def does_player_exists(self, handle: str):
        all_players = self._data.get_all_players()
        for player in all_players:
            if player.handle == handle:
                return True
        
        raise PlayerNotExist

        
            
