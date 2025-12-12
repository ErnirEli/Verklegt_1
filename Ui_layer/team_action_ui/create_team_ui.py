from logic.logic_api import LogicAPI

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

from Ui_layer.ui_constants import UIHelper

#team imports
from Error.team_error import *
from models.team import Team



class CreateTeamUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def create_team(self):
        self._ui.top_bar()
        print(f"{self._ui.RED}{self._ui.BOLD}{"You are creating a team"}")
        print(f"{self._ui.M_LINE}{self._ui.RESET}")
        print("Press q/Q to quit at any time")
        print()
        
        #Name
        while True:
            state = False
            while state == False:
                name = input("Name: ")
                try:
                    state = self._logic.validate_team_name(name)
                except EmptyInput:
                    print("Team needs to have a name")
                except TeamExistsError:
                    print("Team name already exit, team needs an unique name")
                except BackButton:
                    return

            # Web link
            state = False
            while state == False:
                web_link = "https://" + input("Web link: https://")
                try:
                    state = self._logic.validate_team_web_link(web_link)
                except EmptyInput:
                    print("Team needs to have a web link")
                except InvalidWebLink:
                    print("Web link needs to contain a dot")
                except BackButton:
                    return
            #ASCII logo
            state = False
            while state == False:
                ascii = input("ASCII logo: ")
                try:
                    state = self._logic.validate_team_ascii_logo(ascii)
                except EmptyInput:
                    print("Team needs a ASCII logo")
                except BackButton:
                    return
            
            #Number of players in team
            #3-5
            state = False
            while state == False:
                num_of_players = input("Number of players in team: ")
                try:
                    state = self._logic.validate_number_of_players(num_of_players)
                except ValueError:
                    print("Number of players has to be a digit")

                except EmptyInput:
                    print("Team must have 3-5 players")
                except TooManyPlayersError:
                    print("Team can not have more than 5 players")
                except NotEnoughPlayersError:
                    print("Team needs to have at least 3 players")
                except BackButton:
                    return
                
            int(num_of_players)
                

            #Players in team
            num_of_players = int(num_of_players)
            Players_in_team = []
            for _ in range(num_of_players):
                state = False
                while state == False:
                    player_handle = input("Player handle to add to team: ")
                    try:
                        state = self._logic.validate_players_in_team(player_handle, Players_in_team)
                    except PlayerDoesNotExistError:
                        print("Player does not exist")
                    except PlayerAlreadyInTeamError:
                        print("Player already in Team")
                    except playerNotAvailableError:
                        print("Player is already in an another team")
                    except BackButton:
                        return
                    
                Players_in_team.append(player_handle)

            #captain
            state = False
            while state == False:
                captain = input("Choose a captain (handle): ")
                try:
                    state = self._logic.validate_team_captain(captain, Players_in_team)
                except EmptyInput:
                    print("Team needs a captain")
                except CaptainNotExistError:
                    print("Player does not exist")
                except CaptainNotInTeamError:
                    print("Captain is not in the team")
                except BackButton:
                    return


            self._logic.create_team(name, captain, web_link, ascii, Players_in_team)
            print("Team has been created\n")
            print(f"{self._ui.RED}{self._ui.BOLD}{self._ui.M_LINE}{self._ui.RESET}")
            print("1. Create another team\n"
                    "q. back")
            choice = ""
            while choice not in ("1", "q"):
                choice = input("Action: ")
            
            if choice == "q":
                return