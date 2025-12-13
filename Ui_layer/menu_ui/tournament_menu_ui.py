
from Ui_layer.ui_constants import UIHelper

# Ui imports
from Ui_layer.tournament_action_ui.create_tournament_ui import CreateTournamentUI
from Ui_layer.tournament_action_ui.edit_tournament_ui import EditTournamentUI
from Ui_layer.tournament_action_ui.tournament_info import TournamentInfoUI

#Player imports
from Error.player_error import *


class TournamentMenuUI:
    
    def __init__(self):
        self._ui = UIHelper()
        self._create = CreateTournamentUI()
        self._edit = EditTournamentUI()
        self._info = TournamentInfoUI()


    def organizer(self):
        '''Tournament UI for Organizer User. Takes in nothing and returns nothing'''
        
        action = "1"
        while action != "q":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Organizer":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Torunaments":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. Create torunament\n"
                "2. See all tournaments\n"
                "3. See tournament info\n"
                "4. Input match scores\n"
                "q. Back\n\n") 
        
            if action not in ("1", "2", "3", "4"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._create.create_torunamet()
            if action == "2":
                self._info.all_tournaments()
            if action == "3":
                self._info.unrestricted_tournament_info()
            if action == "4":
                self._edit.edit_score()
        return

    def captain(self) -> None:
        '''Torunament UI for captain User. Takes in nothing and returns nothing'''

        action = "1"
        while action != "q":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Captain":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Torunaments":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. See torunament info\n"
                "2. See all tournaments\n"
                "q. Back\n\n") 
        
            if action not in ("1", "2"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._info.restricted_tournament_info()
            if action == "2":
                self._info.all_tournaments()
        return

    def spectator(self) -> None:
        '''Torunament UI for spectator User. Takes in nothing and returns nothing'''
        action = "1"
        while action != "q":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Spectator":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Tournaments":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. See touranment info\n"
                "2. See all torunaments\n"
                "q. Back\n\n") 
        
            if action not in ("1", "2"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._info.restricted_tournament_info()
            if action == "2":
                self._info.all_tournaments()
        return

    