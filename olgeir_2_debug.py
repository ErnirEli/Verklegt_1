# from Datalayer.data_api import DataAPI
# from logic.team_logic import TeamLogic
# from models.team import Team
# from models.player import Player
from Ui_layer.organizer_ui import OrganizerUI
from Ui_layer.Main_menu_ui import MainMenu
from Ui_layer.ui_constants import UIHelper
from Ui_layer.captain_menu import CaptainUI
from Ui_layer.spectator_menu import SpectatorUI

# organizer_ui = OrganizerUI()
# main_menu = MainMenu()
# Ui = UIHelper()


class Main():
    def __init__(self):
        self.organizer_ui = OrganizerUI()
        self.main_menu = MainMenu()
        self.ui_help = UIHelper()
        self.captain_ui = CaptainUI()
        self._spectator = SpectatorUI()

    def main(self):
        
        choice = self.main_menu.show_main_menu()
        while choice != "9":
            if choice == "1":
                self._spectator.spectator_menu()
            if choice == "2":
                self.captain_ui.captain_menu()
            if choice == "3":
                self.organizer_main()
            
            choice = self.main_menu.show_main_menu()


    def organizer_main(self):
        while True:
            first_choice = self.organizer_ui.get_choice()
            if first_choice == "1":
                choice = organizer_ui.player_settings()
                while choice != "9":
                    if choice == "1":
                        choice = organizer_ui.create_player()
                    if choice == "2":        
                        choice = organizer_ui.edit_player_info()
                    if choice == "3":
                        choice = organizer_ui.see_all_players()
                    if choice == "4":
                        choice = organizer_ui.view_player_info()
                        
                    if choice not in ("1", "2", "3", "4", "9"):
                        print("Invalid option")
                    
            
            if first_choice == "2":
                choice = organizer_ui.team_menu()
                if choice == "1":
                    organizer_ui.create_team()
                if choice == "2":
                    organizer_ui.see_all_teams()
                if choice == "3":
                    organizer_ui.see_team_info()
                if choice == "4":
                    organizer_ui.add_player_to_team()
                if choice == "5":
                    organizer_ui.remove_player_from_team()

        if first_choice == "3":
            choice = organizer_ui.club_menu()
            if choice == "1":
                organizer_ui.create_club()
            if choice == "2":
                organizer_ui.see_all_clubs()
            if choice == "3":
                organizer_ui.see_club_info()
            if choice == "4":
                organizer_ui.add_team_to_club()
            if choice == "5":
                organizer_ui.remove_team_from_club()

        if first_choice == "4":
            choice = organizer_ui.tournament_menu()
            if choice == "1":
                organizer_ui.create_tournoment()
            if choice == "2":
                organizer_ui.see_all_tournaments()
            if choice == "3":
                organizer_ui.see_tournament_info()
        
        if first_choice == "9":
            return

hehe = Main()
hehe.main()