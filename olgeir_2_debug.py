# from Datalayer.data_api import DataAPI
# from logic.team_logic import TeamLogic
# from models.team import Team
# from models.player import Player
from Ui_layer.organizer_ui import OrganizerUI
from Ui_layer.Main_menu_ui import MainMenu

yo = OrganizerUI()
main_menu = MainMenu()

while True:
    first_choice = yo.get_choice()
    if first_choice == "1":
        choice = yo.player_settings()
        while choice != "9":
            if choice == "1":
                choice = yo.create_player()
            if choice == "2":        
                choice = yo.edit_player_info()
            if choice == "3":
                choice = yo.see_all_players()
            if choice == "4":
                choice = yo.view_player_info()
                
            if choice not in ("1", "2", "3", "4", "9"):
                print("Invalid option")

            
    
    if first_choice == "2":
        choice = yo.Team_menu()
        if choice == "1":
            yo.create_team()
     
    if first_choice == "3":
        choice = yo.club_menu()
        if choice == "1":
            yo.create_club()
      
    if first_choice == "4":
        siggi = yo.tournament_menu()
        if siggi == "1":
            yo.create_tournoment()
    
    if first_choice == "9":
        main_menu.show_main_menu()