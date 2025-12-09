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

class ValidatePlayer:



    def __init__(self):
        self._data = DataAPI()
    

    def is_captain_or_organizer():
        #Á eftir að implementa
        return
    
    def validate_name(self, name:str):
        if not name or name.strip() == "":
            raise EmptyInput                    # We raise the EmptyInput Exception class only when nothing is input
        return True
    
    def validate_age(self, age: str):
        try:
            age = int(age)
        except ValueError():
            raise WrongAgeException             # Only raised when ValueError is 
        if age < 18 or age > 65:
            raise InvalidAgeException
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
            raise InvalidNumberException
        return True

    def validate_link(self, link: str):
        if not link or link.strip() == "":
            raise EmptyInput
        if "." not in link:
            raise InvalidLinkException
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
            
