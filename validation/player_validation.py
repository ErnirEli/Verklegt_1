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
from models.player import Player

class ValidatePlayer:

    def __init__(self):
        self._data = DataAPI()
    
    def validate_name(self, name: str) -> bool:
        '''Takes a player name of type string and checks if it is valid,
        Raises an error if name is invalid'''

        if name.lower() == "q":
            raise BackButton
        if not name or name.strip() == "":
            raise EmptyInput                    # We raise the EmptyInput Exception class only when nothing is input

        return True
    
    def validate_age(self, dob: str) -> bool:
        '''Takes a player date of birth of type string and checks if it is valid form and if player is 18 years old,
        Raises an error if date of birth or age is invalid'''

        if dob.lower() == "q":
            raise BackButton
        
        if not dob:
            raise EmptyInput 
                    
        if dob.count("-") != 2:
            raise InvalidAgeException
        
        dob: str = dob.split("-")
        try:
            dob = date(int(dob[2]), int(dob[1]), int(dob[0]))
        except ValueError:
            raise DateDoesNotExistError

        today: datetime = datetime.today().date()
        age: datetime = today - dob
        age: int = (age/365.25).days

        if age < 18:
            raise TooYoungError
        
        if age > 99:
            raise TooOldError
        
        return True




    def validate_home_address(self, address: str):
        '''Takes a player adress of type string and checks if it is valid form. 
        Raises an error if adress is invalid'''

        if address.lower() == "q":
            raise BackButton
        
        if not address:
            raise EmptyInput
        
        return True
    

    def validate_email(self, email: str) -> bool:
        '''Takes a player email of type string and checks if it is valid form. 
        Raises an error if eamil is invalid'''

        if email.lower() == "q":
            raise BackButton
        
        if not email or email.strip() == "":
            raise EmptyInput
        
        if "@" not in email or "." not in email:
            raise InvalidEmailException

        return True

    def validate_number(self, number: str) -> bool:
        '''Takes a player number of type string and checks if it is valid form. 
        Raises an error if number is invalid'''

        if number.lower() == "354q":
            raise BackButton
        
        if number == "354":
            raise EmptyInput
        
        if not number.isnumeric() or len(number) != 10:
            raise InvalidNumberError
        
        return True

    def validate_link(self, link: str) -> bool:
        '''Takes a player link of type string and checks if it is valid form. 
        Raises an error if link is invalid'''

        if link.lower() == "q":
            raise BackButton
        
        if link.strip() == "https://":
            raise EmptyInput
        
        if "." not in link:
            raise InvaldlinkException
        
        return True
    
        #eitthvað fleira??

    def validate_handle(self, handle: str) -> bool:
        '''Takes a player handle of type string and checks if it is valid form. 
        Raises an error if handel is invalid'''

        if handle.lower() == "q":
            raise BackButton  
        
        if not handle or handle.strip() == "":
            raise EmptyInput
        
        players: list[Player] = self._data.get_all_players()
        if "," in handle or "/" in handle:
            raise InvalidCharacterHandle
        
        for player in players:
            if player.handle == handle:
                raise HandleExistsException
            
        return True
            
    def does_player_exists(self, handle: str) -> bool:
        '''Takes a player handle of type string and checks if player exists. 
        Raises an error if '''

        all_players: list[Player] = self._data.get_all_players()
        print(all_players)
        for player in all_players:
            print(player.handle, handle)
            if player.handle == handle:
                return True
        
        raise PlayerNotExist

        
            
