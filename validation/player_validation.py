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


class ValidatePlayer:



    def __init__(self, data_wrapper: DataAPI):
        self._data = data_wrapper
    

    def is_captain_or_organizer():
        #Á eftir að implementa
        return
    
    def validate_name(self, name:str):
        if not name or name.strip() == "":
            return (False, "PLayer needs to have a name")
        return True
    
    def validate_age(self, age: str):
        try:
            age = int(age)
        except ValueError():
            return "Please input a number"
        if age < 18 or age > 65: #-----------------------------------------> Ætlum við að hafa age limit??  bæði of amall of ungur?
            return (False, "Player is too young or old to participate")
        return True

    def validate_home_adress(self, adress: str):
        if not adress or adress.strip() == "":
            return (False, "Player needs to have a home adress")
        return True,

    def validate_email(self, email: str):
        if not email or email.strip() == "":
            return (False, "Player needs to have an email")
        if "@" and "." not in email and not isinstance(email, str):
            return (False, "Email is invalid")
        return True,

    def validate_link(self, link: str):
        if not link or link.strip() == "":
            return (False, "Player needs to have a link")
        if link.startswith("https://") == False:
            return (False, "Link is not valid try again")
        return True
        #eitthvað fleira??

    def validate_handle(self, players, handle: str):
        players = self._data.get_all_players()
        for line in players:
            if line.handle == handle:
                return (False, "Player handle needs to be unique")
            if handle == None:
                return (False, "Player needs to have a handle")
            for ch in handle:
                if "," in handle or "/" in handle:
                    return(False, "Username cannot contain , or / in name try again")
        return True
            
