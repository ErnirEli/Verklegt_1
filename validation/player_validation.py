# requirements:
# Name
# age
# home adress
# email
# link
# handle
# team

from data.data_api import DataAPI


class ValidatePlayer:

    def __init__(self):
        pass

    def is_captain_or_organizer():
        #Á eftir að implementa
        return
    
    def validate_name(self, name:str):
        if not name:
            return (False, "PLayer needs to have a name")
    
    def validate_age(self, age: str):
        age = int(age)
        if age < #-----------------------------------------> Ætlum við að hafa age limit??  bæði of amall of ungur?
            return (False, "")
        return True,

    def validate_home_adress(self, adress: str):
        if not adress:
            return (False, "Player needs to have a home adress")
        #Eitthvað miera?

        return True,

    def validate_email(self, email: str):
        if not email:
            return (False, "Player needs to have an email")
        if "@" and "." not in email and not isinstance(email, str):
            return (False, "Email is invalid")
        return True,

    def validate_link(self, link: str):
        if not link:
            return (False, "Player needs to have a link")
        #eitthvað fleira??

    def validate_handle(self, handle: str):
         handle_list = DataAPI.get_all_handles()
         if handle in handle_list:
             return (False, "Player handle needs to be unique")
         if not handle:
             return (False, "Player needs to have a handle")
         return True,
