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
from enum import Enum

""" Validation Class to make all the checks before making
changes or creating players

With each Invalid input we have an error message that follows through
to make it easier for the user to understand where he went wrong as it helps
the overall user experiance"""

class ValidatePlayer:



    def __init__(self, data_wrapper: DataAPI):
        self._data = data_wrapper
    

    def is_captain_or_organizer():
        #Á eftir að implementa
        return
    
    def validate_name(self, name:str):
        if not name or name.strip() == "":                  # We make checks to make sure name is not empty
            return (False, "PLayer needs to have a name")   # Give the user error feedback to make sure he knows whats wrong
        return True,
    
    def validate_age(self, age: str):
        try:
            age = int(age)
        except ValueError():                                # Must be able to change to Int if not its not a valid input
            return (False, "Age must be a number")
        if age < 18 or age > 65:                            # Age validation check since we have an age restriction
            return (False, "Player is too young or old to participate")
        return True,

    def validate_home_adress(self, adress: str):
        if not adress or adress.strip() == "":              # Cannot be an empty input
            return (False, "Player needs to have a home adress")
        return True,

    def validate_email(self, email: str):
        if not email or email.strip() == "":
            return (False, "Player needs to have an email")
        if "@" not in email or "." not in email:            # Making sure included characters are used so email is valid
            return False, "Email is invalid"

        return True,

    def validate_link(self, link: str):
        if not link or link.strip() == "":
            return (False, "Player needs to have a link")
        if link.startswith("https://") == False:            # Link checker so the format inputed is right
            return (False, "Link is not valid try again")
        return True,
        #eitthvað fleira??

    def validate_handle(self, handle: str):
        if not handle or handle.strip() == "":
            raise EmptyHandleException
            return ErrorState.PLAYER_NEEDS_HANDLE
            return (False, "Player needs to have a handle")
        players = self._data.get_all_players()
        if "," in handle or "\"" in handle: 
                             # Make sure some characters are not in the handle to not confuse the database
            raise IllegalCharactersException
            return (False, "Handle contains illegal characters like ',' and '/'")
        for line in players:
            if line.handle == handle:                       # Making sure the Handle that has been inputed isnt already in use
                return (False, "Player handle needs to be unique")
        return True,
            

class ErrorState(Enum):

    PLAYER_NEEDS_HANDLE = 1
    PLAYER_HANDLE_CONTAINS_ILLEGAL_CHARACTERS = 2

try:
    validate_handle...
except EmptyHandleException:
    print("must not be empty")
except IllegalCharactersException:
    print("Handle contains illegal characters")
except Exception:
    print("durrp")



if validate_handle == ErrorState.PLAYER_NEEDS_HANDLE:
    print("error name cannot empty")

class EmptyHandleException(Exception):
    pass

class IllegalCharactersException(Exception):
    pass


