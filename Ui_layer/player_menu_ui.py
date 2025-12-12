from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Ui imports
from Ui_layer.player_action_ui.creat_player_ui import PlayerCreationUI
from Ui_layer.player_action_ui.edit_player_ui import EditPlayerUI
from Ui_layer.player_action_ui.player_info_ui import PlayerInfoUi

# Error imports

#Player imports
from Error.player_error import *


class PlayerMenuUI:
    
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()
        self._create = PlayerCreationUI()
        self._edit = EditPlayerUI()
        self._info = PlayerInfoUi()

    def organizer():
        pass

    def captain(self) -> None:
        '''Player UI for captain User. Takes in nothing and returns nothing'''
        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Captain":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Players":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. Create player\n"
                "2. See player info\n"
                "3. Edit player info\n"
                "4. See all players\n"
                "9. Back\n\n") 
        
            if action not in ("1", "2", "3", "4", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._create.create_player()
            if action == "2":
                self._info.detailed_player_info()
            if action == "3":
                self._edit.edit_player_info()
            if action == "4":
                self._info.all_players()
        return

    def spectator(self) -> None:
        '''Player UI for spectator User. Takes in nothing and returns nothing'''
        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Spectator":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Players":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. See player info\n"
                "2. See all players\n"
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

    