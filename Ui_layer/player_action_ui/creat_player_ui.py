from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

#Player imports
from Error.player_error import *

class PlayerCreationUI:
    def __init__(self):
        self._logic_api = LogicAPI()
        self._ui = UIHelper()
        
    def create_player(self):
        '''Creating a player by asking one information at a time and checking it in Validate Player class'''
        self._ui.top_bar()
        print(f"{self._ui.RED}{self._ui.BOLD}{"You are creating a player"}")
        print(f"{self._ui.M_LINE}{self._ui.RESET}")
        print("Press q/Q to quit at any time")
        print()

        #Name
        while True:
            state = False 
            while state == False: 
                self._ui.top_bar()
                name = input("Name: ")            
                try: 
                    state = self._logic_api.validate_player_name(name)
                except EmptyInput: 
                    print("Player needs to have a name") 
                except BackButton:
                    return 
                

            #Date of Birth
            state = False 
            while state == False: 
                dob = input("Date of birth: in format(Day-month-year): ") 
                try: 
                    state = self._logic_api.validate_player_age(dob) 
                except EmptyInput:
                    print("Player needs to have a date of birth")
                except TooYoungError:
                    print("Player is too young") 
                except TooOldError:
                    print("Player is too old")
                except InvalidAgeException: 
                    print("Date of birth needs to be in the format: day-month-year") 
                except DateDoesNotExistError:
                    print("Date does not exist")
                except BackButton:
                    return

            #Home address 
            state = False 
            while state == False: 
                address = input("Address: ") 
                try: 
                    state = self._logic_api.validate_player_address(address) 
                except EmptyInput: 
                    print("Player needs a home address") 
                except BackButton:
                    return

            #Phone 

            state = False 
            while state == False: 
                number = "354" + input("Phone number: +354 ") 
                try: 
                    state = self._logic_api.validate_player_number(number) 
                except EmptyInput: 
                    print("Player needs a phone number") 
                except InvalidNumberError: 
                    print("Number is invalid, try again")
                except BackButton:
                    return 

            #Email 

            state = False 
            while state == False: 
                email = input("Email: ") 
                try: 
                    state = self._logic_api.validate_player_email(email) 
                except EmptyInput: 
                    print("Player needs to have an email") 
                except InvalidEmailException: 
                    print("Email is invalid, try again") 
                except BackButton:
                    return

            #Link 

            state = False 
            while state == False: 
                link = "https://" + input("Link: https://") 
                try: 
                    state = self._logic_api.validate_player_link(link) 
                except EmptyInput: 
                    print("Player neeeds to have a link") 
                except InvaldlinkException:
                    print("Link has to contain a dot")
                except BackButton:
                    return
                
            #Handle 

            state = False 
            while state == False: 
                handle = input("Handle: ") 
                try: 
                    state = self._logic_api.validate_player_handle(handle) 
                except EmptyInput: 
                    print("Player needs to have a handle") 
                except InvalidCharacterHandle: 
                    print("Handle is invalid, try again") 
                except HandleExistsException: 
                    print("Handle already exists") 
                except BackButton:
                    return

            self._logic_api.create_player(name, dob, address, number, email, link, handle)
            print("Player has been successfully created\n")
            print(f"{self._ui.RED}{self._ui.M_LINE}{self._ui.BOLD}")
            print("1. Create another team\n"
                        "9. back")
            choice = ""
            while choice not in ("1", "9"):
                choice = input("Action: ")
                
            if choice == "9":
                return
            