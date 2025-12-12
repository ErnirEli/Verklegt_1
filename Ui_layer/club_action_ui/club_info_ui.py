from logic.logic_api import LogicAPI

from Ui_layer.ui_constants import UIHelper

# Team imports
from models.team import Team

#Club imports
from Error.club_error import *
from models.club import Club


class ClubInfoUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def see_all_clubs(self) -> None:
        '''UI to show all clubs. Takes in nothing and returns nothing'''
        
        self._ui.top_bar()
        all_clubs: list[Club] = self._logic.list_clubs()
        print("\nAll Clubs:")
        print(f"{"Name":<30}{"Country":<15}{"Tournaments Played":<23}{"Wins":<4}")
        for club in all_clubs:
            print(f"{club.name:<30}{club.country:<15}{club.tournaments:^23}{club.wins:^4}")
        go_back = ""
        while go_back.lower() != "q":
            go_back = input("\nPress q/q to quit")
            
        return

    def see_club_info(self):
        state = False
        while state == False:
            self._ui.top_bar()
            name = input("Enter club name for information (q/Q to quit): ").strip()
            if name.lower() == "q":
                return
            try:
                state = self._logic.does_club_exist(name)
            except ClubDoesNotExist:
                print("Club does not exist")
                return

        club: Club = self._logic.get_club(name)
        teams: list[Team] = self._logic.get_club_teams(club)#To print teams on the bottom
        
        club: Club = self._logic.get_club(name)
        
        self._ui.top_bar()
        print()
        print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*30} Team info {"-"*30}{self._ui.RESET}")
        print(f"{"Name:":<25} {club.name:>45}")
        print(f"{"Color:":<25} {club.color:>45}")
        print(f"{"hometown:":<25} {club.hometown:>45}")
        print(f"{"country:":<10} {club.country:>60}")
        print(f"{"Tournaments played in:":<25} {club.tournaments:>45}")
        print(f"{"Total tournaments second places:":<25} {club.runner_up:>38}\n")
        print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*27} Teams in club {"-"*27}{self._ui.RESET}")
        for team in teams:
            print(f"{"Name:":<25} {team:>45}\n")
        go_back = ""
        while go_back.lower() != "q":
            input("Press Q/q to quit")
        return