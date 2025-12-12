from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Ui imports
from Ui_layer.club_action_ui.club_info_ui import ClubInfoUI
from Ui_layer.club_action_ui.create_club_ui import CreateClubUI
from Ui_layer.club_action_ui.edit_club import EditClubUI
# Error imports

#Player imports
from Error.player_error import *


class ClubMenuUI:
    
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()
        self._info = ClubInfoUI()
        self._create = CreateClubUI()
        self._edit = EditClubUI()

    def organizer(self):
        '''Club UI for Organizer User. Takes in nothing and returns nothing'''
        
        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Organizer":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Clubs":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. Create club\n"
                "2. See club info\n"
                "3. See all clubs\n"
                "4. Add team to club\n"
                "5. Remove team from club\n"
                "9. Back\n\n") 
        
            if action not in ("1", "2", "3", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._create.create_club()
            if action == "2":
                self._info.see_club_info()
            if action == "3":
                self._info.see_all_clubs()
            if action == "4":
                self._edit.add_team()
            if action == "5":
                self._edit.remove_team()
        return

    def captain(self) -> None:
        '''Club UI for captain User. Takes in nothing and returns nothing'''

        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Captain":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Clubs":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. See club info\n"
                "2. See all clubs\n"
                "9. Back\n\n") 
        
            if action not in ("1", "2", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._info.see_club_info()
            if action == "2":
                self._info.see_all_clubs()
        return

    def spectator(self) -> None:
        '''Club UI for spectator User. Takes in nothing and returns nothing'''
        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Spectator":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Clubs":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. See club info\n"
                "2. See all clubs\n"
                "9. Back\n\n") 
        
            if action not in ("1", "2", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._info.see_club_info()
            if action == "2":
                self._info.see_all_clubs()
        return

    