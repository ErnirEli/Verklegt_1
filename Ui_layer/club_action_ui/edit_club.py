from logic.logic_api import LogicAPI
from Ui_layer.ui_constants import UIHelper

# Error
from Error.general_error import BackButton
from Error.club_error import *

# Model imports
from models.club import Club
from models.team import Team


class EditClubUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def add_team(self) -> None:
        '''UI for adding a team to a club, takes in nothing and returns nothing'''
        self._ui.top_bar()
        while True:
            state = False
            while state == False:
                club_name = input("Enter club name to add teams to (q/Q to quit): ")
                if club_name.lower() == "q":
                    return
                
                try:
                    state = self._logic.does_club_exist(club_name)
                except ClubDoesNotExist:
                    print("Club does not exist")

            club: Club = self._logic.get_club(club_name)
            teams_in_club: list[Team] = self._logic.get_club_teams(club)
            
            if len(teams_in_club) > 5:
                print("Club is full")
                continue
                
            state = False
            while state == False:
                team_name = input("Enter team name to add to club (q/Q to quit): ")
                try:
                    state = self._logic.validate_teams_in_club(team_name)
                except TeamDoesNotExistError:
                    print("Team does not exist")
                except BackButton:
                    return
                except TeamNotAvailableError:
                    print("Team is already in a club")
                

            
            team: Team = self._logic.get_team(team_name)
            

            self._logic.add_team(club, team)
            print("Team added to club")

            return

    def remove_team(self) -> None:
        '''UI for removing a player from a club, takes in nothign and returns nothing'''
        while True:
            state = False
            while state == False:
                self._ui.top_bar()
                club_name = input("Enter club name to remove teams from(q/Q to quit): ")
                if club_name.lower() == "q":
                    return
                
                try:
                    state = self._logic.does_club_exist(club_name)
                except ClubDoesNotExist:
                    print("Club does not exist")
            
            

            club: Club = self._logic.get_club(club_name)
            teams_in_club: list[Team] = self._logic.get_club_teams(club)
            
            if len(teams_in_club) < 2:
                print("The club does not have enough teams to remove one")
                continue
                
            state = False
            while state == False:
                team_name = input("Enter team name to remove from club (q/Q to quit): ")
                if team_name.lower() == "q":
                    return
                try:
                    state = self._logic.validate_club_to_remove(team_name)
                except TeamDoesNotExistError:
                    print("Team does not exist")
                


            
            team: Team = self._logic.get_team(team_name)
            if team.name not in teams_in_club:
                print("Team is not in the Club")
                continue
            
            

            self._logic.remove_team(team)
            print("Player has been removed from the club")

            return