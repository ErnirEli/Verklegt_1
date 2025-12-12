# from Datalayer.data_api import DataAPI
# from logic.team_logic import TeamLogic
# from models.team import Team
# from models.player import Player
from Ui_layer.organizer_ui import OrganizerUI
from Ui_layer.Main_menu_ui import MainMenu
from Ui_layer.ui_constants import UIHelper
from Ui_layer.captain_menu import CaptainUI
from Ui_layer.spectator_menu import SpectatorUI
from Ui_layer.organizer_menu import OrganizerUI

# self.organizer_ui = OrganizerUI()
# main_menu = MainMenu()
# Ui = UIHelper()


class Main():
    def __init__(self):
        self._main_menu = MainMenu()
        self._ui = UIHelper()
        self._captain = CaptainUI()
        self._spectator = SpectatorUI()
        self._organizer = OrganizerUI()

    def main(self):
        
        choice = self._main_menu.show_main_menu()
        while choice != "q":
            if choice == "1":
                self._spectator.spectator_menu()
            if choice == "2":
                self._captain.captain_menu()
            if choice == "3":
                self._organizer.organizer_menu()
            
            choice = self._main_menu.show_main_menu()

hehe = Main()
hehe.main()

