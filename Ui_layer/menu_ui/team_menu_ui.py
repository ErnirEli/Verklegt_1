from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Ui imports
from Ui_layer.team_action_ui.create_team_ui import CreateTeamUI
from Ui_layer.team_action_ui.edit_team_ui import EditTeamUI
from Ui_layer.team_action_ui.team_info_ui import TeamInfoUI

# Error imports

#Player imports
from Error.team_error import *


class TeamMenuUI:
    
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()
        self._create = CreateTeamUI()
        self._edit = EditTeamUI()
        self._info = TeamInfoUI()


    def organizer(self):
        '''Team UI for Organizer User. Takes in nothing and returns nothing'''
        
        action = "1"
        while action != "q":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Organizer":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Teams":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. Create Team\n"
                "2. See all teams\n"
                "3. See team info\n"
                "4. Add player to team\n"
                "5. Remove player from team\n"
                "q. Back\n\n") 
        
            if action not in ("1", "2", "3", "4", "5"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._create.create_team()
            if action == "2":
                self._info.see_all_teams()
            if action == "3":
                self._info.see_team_info()
            if action == "4":
                self._edit.add_player()
            if action == "5":
                self._edit.remove_player()
        return

    def captain(self) -> None:
        '''Player UI for captain User. Takes in nothing and returns nothing'''
        action = "1"
        while action != "q":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Captain":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Teams":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. See all teams\n"
                "2. See team info\n"
                "3. Add player to team\n"
                "4. Remove player from team\n"
                "9. Back\n\n") 
        
            if action not in ("1", "2", "3", "4", "9"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            
            if action == "1":
                self._info.see_all_teams()
            if action == "2":
                self._info.see_team_info()
            if action == "3":
                self._edit.add_player()
            if action == "4":
                self._edit.remove_player()

        return

    def spectator(self) -> None:
        '''Player UI for spectator User. Takes in nothing and returns nothing'''
        action = "1"
        while action != "q":
            self._ui.top_bar()
            print(f"\n"
                f"{self._ui.BOLD}{self._ui.RED}{"Spectator":^20}\n"
                f"{self._ui.M_LINE}{self._ui.RESET}\n"
                f"{"Teams":^20}\n"
                f"{self._ui.M_LINE}\n"
                "1. See all teams\n"
                "2. See team info\n"
                "q. Back\n\n") 
        
            if action not in ("1", "2"):
                action = input("Please select a valid action: ")
            else:
                action = input("Please select an action: ")
            if action == "1":
                self._info.see_all_teams()
            if action == "2":
                self._info.see_team_info()
        return

    