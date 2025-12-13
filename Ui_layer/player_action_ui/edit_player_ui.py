from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

from Error.general_error import BackButton

#Player imports
from Error.player_error import *


class EditPlayerUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def edit_player_info(self):
        
            state = False
            while state == False:
                self._ui.top_bar()
                handle = input("Please provide the handle of the player you want to modify (q/q to quit): ").strip()
                if handle.lower() == "q":
                    return
                try:
                    state = self._logic.does_player_exists(handle)
                except PlayerNotExist:
                    print("Player does not exist")
                except BackButton:
                    return

            player = self._logic.find_player(handle)
            self._ui.top_bar()
            
            
            print(f"\n{"-"*27} Current player info {"-"*27}")
           
            print(f"{"Phone number:":<25}{player.phone:>48}")
            print(f"{"Email:":<25}{player.email:>48}")
            print(f"{"Address:":<25}{player.address:>48}")
            print(F"{"Link:":<25}{player.link:>48}")
            
        

            print("\nLeave edit inputs empty if you don't want to change them (Q/q to quit): \n")

            #New phone
            while True:
                raw_phone = "354" + input("New phone (empty to keep current): +354").strip()
                if raw_phone == "354":
                    new_phone = None
                    break

                try:
                    self._logic.validate_player_number(raw_phone)
                    new_phone = raw_phone
                    break

                except InvalidNumberError:
                    print("Number is invalid, try again.")

                except BackButton:
                    return
            

            #New email
            while True:
                raw_email = input("New email (empty to keep current): ")
                if raw_email == "":
                    new_email = None
                    break

                try:
                    self._logic.validate_player_email(raw_email)
                    new_email = raw_email
                    break
                except InvalidEmailException:
                    print("Email is invalid, try again.")
                except BackButton:
                    return

            #New address
            while True:
                raw_address = input("New address (empty to keep current): ")
                if raw_address == "":
                    new_address = None
                    break
                try:
                    self._logic.validate_player_address(raw_address)
                    new_address = raw_address
                    break
                except BackButton:
                    return
                    

            #New link
            while True:
                raw_link = input("New link (empty to keep current): https://")
                if raw_link == "":
                    new_link = None
                    break

                try:
                    self._logic.validate_player_link(raw_link)
                    new_link = "https://" + raw_link
                    break

                except InvalidLinkException:
                    print("Link is invalid, try again (must start with https:// and contain a dot).")
                except BackButton:
                    return

            state = self._logic.edit_player_info(
                handle,
                new_phone=new_phone,
                new_email=new_email,
                new_address=new_address,
                new_link=new_link,
            )

            print("Modifications to player info have been made.")
            
            return 

