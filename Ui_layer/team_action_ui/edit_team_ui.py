from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Error imoprts
from Error.general_error import BackButton
from Error.team_error import *

# Model imports
from models.team import Team
from models.player import Player


class EditTeamUI():
    pass
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()
        pass

    def remove_player(self):
        '''UI for removing player from a team. Takes in nothing and Returns nothing'''

        while True:
            state = False
            while state == False:
                self._ui.top_bar()
                team_name = input("Enter team name to remove players from (q/Q to quit): ")
                if team_name.lower() == "q":
                    return
                try:
                    state = self._logic.does_team_exists(team_name)
                except TeamExistsError:
                    print("Team does not exist")
            

            players_in_team: list[Player] = self._logic.get_team_players(team_name)
            
            
            if len(players_in_team) < 4:
                print("There are too few players in the team to remove from it")
                continue #go back to the top
                
            team: Team = self._logic.get_team(team_name)#Goes in validation to check if captain is removed

            
            while True: 
                player_name = input("Enter player handle to remove from team (q/Q to quit): ")
                try:
                    self._logic.validate_player_to_remove(player_name, team)
                    
                except PlayerDoesNotExistError:
                    print("Player does not exist")
                    continue
                except BackButton:
                    return
                except CantRemoveCaptainError:
                    print("Captain can not be removed")
                    continue

                player: Player= self._logic.find_player(player_name)
                if player.handle not in players_in_team:
                    print(player.name)
                    print(players_in_team)
                    print("player is not in the team")
                else:
                    break    
        
            self._logic.remove_player(player)
            print("Player has successfully been removed from\n")
            print(f"{self._ui.RED}{self._ui.BOLD}{self._ui.M_LINE}{self._ui.RESET}")
            print("1. Remove another player\n"
                    "q. back\n")
            choice = ""
            while choice not in ("1", "q"):
                choice = input("Action: ")
            
            if choice == "q":
                return



    def add_player(self) -> None:
        '''UI for adding player to a team. Takes in nothing and Returns nothing'''

        while True:
            state = False
            while state == False:
                self._ui.top_bar()
                team_name = input("Enter team name to add players to (q/Q to quit): ")
                if team_name.lower() == "q":
                    return
                try:
                    state = self._logic.does_team_exists(team_name)
                except TeamExistsError:
                    print("Team does not exist")


            players_in_team = self._logic.get_team_players(team_name)
            
            if len(players_in_team) > 5:
                print("Team is full")
                continue
                
            state = False
            while state == False:
                player_name = input("Enter player handle to add to team (q/Q to quit): ")
                try:
                    state = self._logic.validate_players_in_team(player_name, players_in_team)
                except PlayerDoesNotExistError:
                    print("Player does not exist")
                except playerNotAvailableError:
                    print("Player is Already in a team")
                except BackButton:
                    return
            
            team: Team = self._logic.get_team(team_name)
            player: Player = self._logic.find_player(player_name)
        
            self._logic.add_player(team, player)
            print("Player has successfully been added to the team\n")
            print(f"{self._ui.RED}{self._ui.BOLD}{self._ui.M_LINE}{self._ui.RESET}")
            print("1. Add another player\n"
                    "q. back\n")
            choice = ""
            while choice not in ("1", "q"):
                choice = input("Action: ")
            
            if choice == "q":
                return
