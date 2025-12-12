from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Ui imports
from Ui_layer.menu_ui.player_menu_ui import PlayerMenuUI
from Ui_layer.menu_ui.team_menu_ui import TeamMenuUI
from Ui_layer.menu_ui.club_menu_ui import ClubMenuUI
from Ui_layer.menu_ui.tournament_menu_ui import TournamentMenuUI

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

#Player imports
from Error.player_error import *
from models.player import Player


class CaptainUI:
    def __init__(self):
        self._logic_api = LogicAPI()
        self._ui = UIHelper()
        self._player_ui = PlayerMenuUI()
        self._team_ui = TeamMenuUI()
        self._club_ui = ClubMenuUI()
        self._torunament_ui = TournamentMenuUI()

    def organizer_menu(self):
        action = "1"
        while action != "9":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Organizer":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                "1. Player menu\n"
                "2. Team menu\n"
                "3. Club menu\n"
                "4. Tournament menu\n"
                "9. Change role\n\n") 
            
            if action not in ("1", "2", "3", "4", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._player_ui.organizer()
            if action == "2":
                self._team_ui.organizer()
            if action == "3":
                self._club_ui.organizer()
            if action == "4":
                self._tournament_ui.organizer()           

            
        return

