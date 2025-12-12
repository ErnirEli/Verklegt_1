from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

#Player imports
from Error.player_error import *
from models.player import Player



class PlayerInfoUi:
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def all_players(self):
        all_players: list[Player] = self._logic.list_players()
        self._ui.top_bar()
        print("All players:")
        print(f"{"Name":<30}{"Handle":<32}{"Date of birth":<20}{"Team name":<8}")
        for player in all_players:
            print(f"{player.name:<29} {player.handle:<31} {player.dob:<19} {player.team_name:<7}")



        go_back = ""
        while go_back.lower() != "q":
            go_back = input("Press q/q to quit: ")
            
        return
    
    def detailed_player_info(self):
        #self._ui.top_bar()
        handle = input("Enter player handle (q/Q to quit): ").strip()
        while handle.lower() != "q":
            #self._ui.top_bar()
            player: Player = self._logic.find_player(handle)
            if player is None:
                print("No player found with that handle.")
            
            else:
                print(f"\n{"-"*30} Player info {"-"*30}")
                print(f"{"Handle:":<25}{player.handle:>48}")
                print(f"{"Team name:":<25}{player.team_name:>48}")
                print(f"{"Date og birht:":<25}{player.dob:>48}")
                print(f"{"Address:":<25}{player.address:>48}")
                print(f"{"Phone number:":<25}{player.phone:>48}")
                print(f"{"Email:":<25}{player.email:>48}")
                print(F"{"Link:":<25}{player.link:>48}")
                print(f"{"Total tournaments played in:":<50}{player.tournament:>23}")
                print(f"{"Tournamnets won:":<25}{player.wins:>48}")
                print()
            
            handle = input("Enter player handle (q/Q to quit): ").strip()



        return
    def player_info(self):
        handle = ""
        while handle.lower() != "q":
            self._ui.top_bar()
            handle = input("Enter player handle (q/Q to quit): ").strip()
            player: Player = self._logic.find_player(handle)
            if player is None:
                print("No player found with that handle.")
            
            else:
                print(f"\n{"-"*30} Player info {"-"*30}")
                print(f"{"Handle:":<25}{player.handle:>48}")
                print(f"{"Team name:":<25}{player.team_name:>48}")
                print(F"{"Link:":<25}{player.link:>48}")
                print(f"{"Total tournaments played in:":<50}{player.tournament:>23}")
                print(f"{"Tournamnets won:":<25}{player.wins:>48}")
                print()