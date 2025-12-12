from logic.logic_api import LogicAPI

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

from Ui_layer.ui_constants import UIHelper

#Player imports
from Error.player_error import *
from models.player import Player

#Tournaments imports
from Error.tournament_error import *
from models.tournament import Tournament

#team imports
from Error.team_error import *
from models.team import Team

#Club imports
from Error.club_error import *


class CreateClubUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def create_club(self) -> None:
        '''UI for creating a class, takes in nothing and returns nothing'''

        self._ui.top_bar()
        print(f"{self._ui.RED}{self._ui.BOLD}{"You are creating a club"}")
        print(f"{self._ui.M_LINE}{self._ui.RESET}")
        print("Press q/Q to quit at any time")
        print()

        #name
        state = False
        while state == False:
            name = input("Name: ")
            try:
                state = self._logic.validate_club_name(name)
            except EmptyInput:
                print("Club needs to have a name")
            except ClubNameExistsError:
                print("Name already exissts, club needs to have an unique name")
            except BackButton:
                return

        #Colors
        state = False
        print("Available colors: [blue, light blue, red, light red, orange, green, light green, yellow, black, white, brown, purple, light purple, cyan, light cyan, light gray, dark gray]")
        while state == False:
            color = input("Choose 1 color: ")
            try:
                state = self._logic.validate_club_colors(color)
            except EmptyInput:
                print("Club needs to have at least one color")
            except ColorNotAvailable:
                print("Color not available")
            except BackButton:
                return
        #Hometown
        state = False
        while state == False:
            hometown = input("Hometown: ")
            try:
                state = self._logic.validate_club_hometown(hometown)
            except EmptyInput:
                print("Club needs to have a hometown")
            except BackButton:
                return
        
        #Country
        state = False
        while state == False:
            country = input("Country: ")
            try:
                state = self._logic.validate_club_country(country)
            except EmptyInput:
                print("Club needs to have a country")
            except BackButton:
                return
            

        #Number of tems in club
        state = False
        while state == False:
            num_of_teams = input("Number of teams in club:")
            try:
                state = self._logic.validate_num_of_teams(num_of_teams)
            except ValueError:
                print("Number of teams have to be a digit")
            except InvalidNumOfTeams:
                print("Club can only have 1-5 teams")
            except BackButton:
                return
        num_of_teams = int(num_of_teams)
        
        
        
        

        #Teams in club
        teams_in_club = []
        for _ in range(num_of_teams):
            
            
            state = False
            while state == False:
                team_to_club = input("Team in club: ")
                try:
                    state = self._logic.validate_teams_in_club(team_to_club, teams_in_club)
                except TeamDoesNotExistError:
                    print("Team does not exist")
                except TeamAlreadyInClubError:
                    print("Team is already in the club")
                except TeamNotAvailableError:
                    print("Team is already in an another club")
                except BackButton:
                    return
            teams_in_club.append(team_to_club)
            



        self._logic.create_club(name, color, hometown, country, teams_in_club)
