from logic.logic_api import LogicAPI

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

from Ui_layer.ui_constants import UIHelper

#Player imports
from models.player import Player

#team imports
from Error.team_error import *
from models.team import Team


class TeamInfoUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def see_all_teams(self):
        all_teams: list[Team] = self._logic.list_teams()
        print("\nAll Teams:")
        print(f"{"Name":<30}{"Club":<15}{"Tournaments Played":^23}{"Wins":<4}")
        for team in all_teams:
            print(f"{team.name:<30}{team.club:<15}{team.tournament:^23}{team.wins:^4}")

        go_back = ""
        while go_back.lower() != "q":
            go_back = input("Press q/q to quit")
            
        return

    def see_team_info(self):
        state = False
        while state == False:
            name = input("Enter team name for information (q/Q to quit): ").strip()
            if name.lower() == "q":
                return
            try:
                state = self._logic.does_team_exists(name)
            except TeamDoesNotExist:
                print("Team does not exist")
                return self.see_team_info()

            players:list[Player] = self._logic.get_team_players(name)#To print players on the bottom

            team: Team = self._logic.get_team(name)
            
        
        
            print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*30} Team info {"-"*30}{self._ui.RESET}")
            print(f"{"Name:":<25} {team.name:>45}")
            print(f"{"Captain:":<25} {team.captain:>45}")
            print(f"{"Club:":<25} {team.club:>45}")
            print(f"{"Web link:":<10} {team.web_link:>60}")
            print(f"{"ASCII logo:":<25} {team.ASCII:>45}")
            print(f"{"Tournaments Played in:":<25} {team.tournament:>45}")
            print(f"{"Tournaments won:":<25} {team.wins:>45}")
            print(f"{"Total tournaments second places:":<25} {team.runner_up:>38}\n")
            print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*27} Players in team {"-"*27}{self._ui.RESET}")
            for player in players:
                print(f"{"Name:":<25} {player:>45}")

        action = ""
        while action.lower() != "q":
            action = input("Press Q/q to quit: ")
    
        return