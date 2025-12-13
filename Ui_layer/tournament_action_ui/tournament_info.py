from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

#Error imports
from Error.tournament_error import *
from Error.player_error import *
from Error.team_error import *
from Error.club_error import *



#Model imports
from models.match import Match
from models.tournament import Tournament


class TournamentInfoUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def unrestricted_tournament_info(self) -> None:
        '''Ui to show tournament info and schedule, takes in nothin and returns nothing'''
        state = False
        while state == False:
            self._ui.top_bar()
            id = input("Enter Tournament ID for information (q/Q to quit): ").strip()
            if id.lower() == "q":
                return
            try:
                state = self._logic.does_tournament_id_exist(id)
            except TournamentNotExistError:
                print("Tournament does not exist")
                continue

        tournament: Tournament = self._logic.get_tournament(id)
        
        self._ui.top_bar()
        print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*27} Tournament info {"-"*27}{self._ui.RESET}")
        print(f"{"ID:":<25} {tournament.id:>45}")
        print(f"{"name:":<25} {tournament.name:>45}")
        print(f"{"venue:":<25} {tournament.venue:>45}")
        print(f"{"Start date:":<25} {tournament.start_date:>45}")
        print(f"{"End date:":<25} {tournament.end_date:>45}")
        print(f"{"Contract:":<25} {tournament.contact:>45}\n")
        print(f"{"Contact email:":<25} {tournament.contact_email:>45}")
        print(f"{"Contact Phone number:":<25}{tournament.contact_number:>45}")
        print(f"{"State:":<24} {str(tournament.state):>45}")
        print(f"{"Servers":<25}{len(tournament.servers):>45}")            
        
        print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*24} Matches in tournament {"-"*24}{self._ui.RESET}")
            
        all_matches: list[Match] = self._logic.list_matches()

        for match in all_matches:
            if match.tournament_id == id:
                print(match)

        go_back = ""
        while go_back.lower() != "q":
            go_back =input("\nPress Q/q to quit ")
        
        return

    def restricted_tournament_info(self):
        '''Ui function to display restricted tournament info. Takes in nothing and retuns nothing.
        Handles inputs, prints and error handeling'''

        state = False
        while state == False:
            self._ui.top_bar()
            id = input("Enter Tournament ID for information (q/Q to quit): ").strip()
            if id.lower() == "q":
                return
            try:
                state = self._logic.does_tournament_id_exist(id)
            except TournamentNotExistError:
                print("Tournament does not exist")
                continue

            tournament: Tournament = self._logic.get_tournament(id)
            
            self._ui.top_bar()
            print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*27} Tournament info {"-"*27}{self._ui.RESET}")
            print(f"{"ID:":<25} {tournament.id:>45}")
            print(f"{"name:":<25} {tournament.name:>45}")
            print(f"{"venue:":<25} {tournament.venue:>45}")
            print(f"{"Start date:":<25} {tournament.start_date:>45}")
            print(f"{"End date:":<25} {tournament.end_date:>45}")
            print(f"{"State:":<24} {str(tournament.state):>45}")
            
            print(f"\n{self._ui.BOLD}{self._ui.RED}{"-"*24} Matches in tournament {"-"*24}{self._ui.RESET}")
                
            all_matches: list[Match] = self._logic.list_matches()

            for match in all_matches:
                if match.tournament_id == id:
                    print(match)

            go_back = ""
            while go_back.lower() != "q":
                go_back =input("\nPress Q/q to quit ")
            
            return


    def all_tournaments(self) -> None:
        '''UI to show all tournaments, takes in nothing and returns nothing'''
        all_tournaments: list[Tournament] = self._logic.list_tournaments()
        self._ui.top_bar()
        print("\nAll Tournamnets:")
        print(f"{"Name":<60}{"ID":<18}{"State":<15}")
        for tournament in all_tournaments:
            print(f"{tournament.name:<60}{tournament.id:<18}{str(tournament.state):<15}")
            
        go_back = ""
        while go_back.lower() != "q":
            go_back = input("\nPress Q/q to quit ")
            
        return