# UI's
from Ui_layer.Main_menu_ui import MainMenu
from Ui_layer.ui_constants import UIHelper

# Roles
from Ui_layer.captain_menu import CaptainUI
from Ui_layer.spectator_menu import SpectatorUI
from Ui_layer.organizer_menu import OrganizerUI


class Main():
    def __init__(self):
        self._main_menu = MainMenu()
        self._ui = UIHelper()
        self._captain = CaptainUI()
        self._spectator = SpectatorUI()
        self._organizer = OrganizerUI()

    def main(self):
        
        choice: str = self._main_menu.show_main_menu()
        while choice != "q":
            if choice == "1":
                self._spectator.spectator_menu()
            if choice == "2":
                self._captain.captain_menu()
            if choice == "3":
                self._organizer.organizer_menu()
            
            choice: str = self._main_menu.show_main_menu()

main = Main()
main.main()

