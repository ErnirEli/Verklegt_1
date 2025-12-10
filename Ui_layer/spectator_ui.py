from logic.logic_api import logicAPI
from random import choice
from typing import Dict, Type, Optional

from lagaui import Captain, ChangeRole, CreateAClub, CreateAPlayer, CreateATournament, Organiser, SeeMatchResult, SeeMatchSchedule, SeeTournament, UIlayer, ViewTeams
from ui2 import players
#import validation að hvert og allt virkar from import validation...
from validation.player_validation import ValidatePlayer
from logic.player_logic import PlayerLogic
 

class Spectator:
    "(Áhorfandi) getur séð allt eins og t.d leikjadagskrá, úrslit, liðin, upplysíngar um lið, leikmenn, upplysíngar um leikmenn " 
    def __init__(self):
        self._logic = logicAPI()

    def __str__(self):
        return (
            "Spectator\n"
            "-------------\n"
            "1. View Teams\n"
            "2. See Tournaments\n"
            "3. See match schedule\n"
            "4. See results\n"
            "5. View players\n\n"
            "9. Change role\n"
            "---------------\n"
        )
     
    
    def get_choice(self):
        """Ask user and return a validated choice."""
        while True:
            print(self)
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "5", "6" "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")

    def run(self):
        while True:

            if Spectator.get_choice == "1":
                players = self._logic.list_players_public()
                print("\n--- Players ---")
                for p in players:
            # p is a dict: {'handle': '...', 'team_name': '...'}
                    print(f"Handle: {p['handle']}")
                    print(f"Team name: {p['team_name']}")
                    print("-" * 35)
            
            elif choice == "2":
                handle = input("Enter player handle: ").strip()
                player = self._logic.get_player_public_info(handle)
                if player is None:
                    print("No player found with that handle.")
                else:
        
                    print("\n--- Player info ---")
                    print(f"Handle: {player['handle']}")
                    print(f"Team name: {player['team_name']}")