
from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Ui imports

# Error imports

#Player imports
from Error.player_error import *


class TournamentMenuUI:
    
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()


    def organizer(self):
        '''Tournament UI for Organizer User. Takes in nothing and returns nothing'''
        
        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Organizer":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Torunaments":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. Create torunament\n"
                "2. See club info\n"
                "3. See all clubs\n"
                "9. Back\n\n") 
        
            if action not in ("1", "2", "3", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._create.create_player()
            if action == "2":
                self._info.detailed_player_info()
            if action == "3":
                self._edit.edit_player_info()
        return

    def captain(self) -> None:
        '''Torunament UI for captain User. Takes in nothing and returns nothing'''

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
                self._create.create_player()
            if action == "2":
                self._info.detailed_player_info()
        return

    def spectator(self) -> None:
        '''Torunament UI for spectator User. Takes in nothing and returns nothing'''
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
                self._info.player_info()
            if action == "2":
                self._info.all_players()
        return

    