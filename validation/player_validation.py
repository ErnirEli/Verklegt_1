# requirements:
# Name
# age
# home adress
# email
# link
# handle
# team

from Datalayer.data_api import DataAPI


class ValidatePlayer:



    def __init__(self):
        self._data = DataAPI()
    

    def is_captain_or_organizer():
        #Á eftir að implementa
        return
    
    def validate_name(self, name:str):
        if not name or name.strip() == "":
            return (False, "Player needs to have a name")
        return True,
    
    def validate_age(self, age: str):
        #if not age.isnumeric():
        
        try:
             age = int(age)
        except ValueError:
            return (False, "Age must be a number, try again")
        if age < 18 or age > 65: #-----------------------------------------> Ætlum við að hafa age limit??  bæði of amall of ungur?
            return (False, "Player is too young or old to participate")
        return True,

    def validate_home_adress(self, adress: str):
        if not adress or adress.strip() == "":
            return (False, "Player needs to have a home adress")
        return True,

    def validate_phone(self, phone: str):
        if phone == "354":
            return (False, "Player needs to have a phone number")
        if not phone.isnumeric() or len(phone) != 10:
            return (False, "Phone number is ivalid, try again")
        return True,

    def validate_email(self, email: str):
        if not email or email.strip() == "":
            return (False, "Player needs to have an email")
        if "@" not in email or "." not in email:
            return (False, "Email is invalid, try again")

        return True,

    def validate_link(self, link: str):
        if not link or link.strip() == "":
            return (False, "Player needs to have a link")
        if link.startswith("https://") == False:
            return (False, "Link is not valid, try again")
        if "." not in link:
            return (False, "Link is not valid, try again")
        return True,
        #eitthvað fleira??

    def validate_handle(self, handle: str):
        if not handle or handle.strip() == "":
            return (False, "Player needs to have a handle")
        players = self._data.get_all_players()
        if "," in handle or "/" in handle:
            return (False, "Handle contains illegal characters like ',' and '/', try again")
        for line in players:
            if line.handle == handle:
                return (False, "Player handle needs to be unique, try again")
        return True,
