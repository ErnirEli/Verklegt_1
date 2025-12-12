from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Ui imports
from Ui_layer.player_ui import PlayerUi
from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

#Player imports
from Error.player_error import *
from models.player import Player


class SpectatorUI:
    def __init__(self):
        self._logic_api = LogicAPI()
        self._ui = UIHelper()
        self.player_ui = PlayerUi()

    def spectator_menu(self):
        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Spectator":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                "1. Player settings\n"
                "2. Team menu\n"
                "3. Club menu\n"
                "4. Tournament menu\n"
                "9. Change role\n\n") 
            
            if action not in ("1", "2", "3", "4", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self.player_ui.spectator()
                continue
            if action == "2":
                pass
            if action == "3":
                pass
            if action == "4":
                pass

            
        return

