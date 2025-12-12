from logic.logic_api import LogicAPI

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

from Ui_layer.ui_constants import UIHelper

#Player imports
from validation.player_validation import ValidatePlayer
from logic.player_logic import PlayerLogic
from Error.player_error import *
from models.player import Player

#Tournaments imports
from validation.tournament_validation import ValidateTournament
from logic.tournament_logic import TournamentLogic
from Error.tournament_error import *
from models.tournament import Tournament

#team imports
from logic.team_logic import TeamLogic
from validation.team_validation import ValidateTeam
from Error.team_error import *
from models.team import Team

#Club imports
from logic.club_logic import ClubLogic
from validation.club_validation import ValidateClub
from Error.club_error import *
from models.club import Club

#Match imports
from models.match import Match
from Error.match_error import InvalidScores, DrawError
from validation.match_validation import ValidateMatch

#schedule imports

class EditTournamentUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def edit_score(self):
        '''Ui for edititng score from games in a tournament, takes in nothing and returns nothing,
        Handles inputs, prints and errors'''
        
        state = False
        while state == False:
            self._ui.top_bar()
            id = input("Enter Tournament ID for inputin match results (q/Q to quit): ").strip()
            if id.lower() == "q":
                return 
            try:
                state = self._logic.does_tournament_id_exist(id)
            except TournamentNotExistError:
                print("Tournament does not exist")
                continue
        

        back_button = ""
        while back_button.lower() != "q":
        
            tournament: Tournament = self._logic.get_tournament(id)
            if tournament.state == True:
                print("Tournament is finished")
                return
            
            all_matches: list[Match] = self._logic.get_active_matches(tournament)
        

            for match in all_matches:
                if match.state == True:
                    continue
                print(f"Match {match.match_number}")
                state = False
                while state == False:
                    a_score = input(f"{match.team_a} = ")
                    b_score = input(f"(Q/q to quit) {match.team_b} = ")
                    try:
                        state = self._logic(a_score, b_score)
                    except ValueError:
                        print("Invalid, scores have to be a number")
                    except InvalidScores:
                        print("Invalid, scores can only be from 0-99")
                    except DrawError:
                        print("Game ended in a draw")
                        print("Enter in result after extra time")
                    except BackButton:
                        return self.tournament_menu()
                
                
                self._logic.update_game_results(match, a_score, b_score)
            
        
        
            back_button = input("\nAll matcehs in this round are done, Press Q/q to quit, Press enter for the next round")
            
        return
