# from Datalayer.data_api import DataAPI
# from logic.team_logic import TeamLogic
# from models.team import Team
# from models.player import Player
from Ui_layer.organizer_ui import OrganizerUI
from Ui_layer.Main_menu_ui import MainMenu
organizer_ui = OrganizerUI()
main_menu = MainMenu()

while True:
    first_choice =organizer_ui.get_choice()
    if first_choice == "1":
        choice =organizer_ui.player_settings()
        while choice != "9":
            if choice == "1":
                choice =organizer_ui.create_player()
            if choice == "2":        
                choice =organizer_ui.edit_player_info()
            if choice == "3":
                choice =organizer_ui.see_all_players()
            if choice == "4":
                choice =organizer_ui.view_player_info()

            if choice not in ("1", "2", "3", "4", "9"):
                print("Invalid option")

            
    
    if first_choice == "2":
        choice =organizer_ui.team_menu()
        while choice != "9":

        
            if choice == "1":
                choice = organizer_ui.create_team()
            if choice == "2":
                choice = organizer_ui.see_all_teams()
            if choice == "3":
                choice = organizer_ui.see_team_info()
        
    if first_choice == "3":
            
            choice =organizer_ui.club_menu()
            if choice == "1":
                organizer_ui.create_club()
            if choice == "2":
                organizer_ui.see_all_clubs()
            if choice == "3":
                organizer_ui.see_club_info()
        
    if first_choice == "4":
            
            siggi =organizer_ui.tournament_menu()
            if siggi == "1":
                organizer_ui.create_tournoment()
                organizer_ui.create_tournoment()
        
    if first_choice == "9":
        main_menu.show_main_menu()


#club info i show all:
#Name,country, tournament, wins


#Tournament info i show all:
#Name, venue, id