from logic.logic_api import LogicAPI

from Error.general_error import EmptyInput, DateDoesNotExistError, BackButton

from Ui_layer.ui_constants import UIHelper


from Error.tournament_error import *

#

class CreateTournamentUI():
    def __init__(self):
        self._logic = LogicAPI()
        self._ui = UIHelper()

    def create_torunamet(self) -> None:
        '''Ui for tournament creation, takes in nothing and returns nothing'''
        self._ui.top_bar()
        print(f"{self._ui.RED}{self._ui.BOLD}{"You are creating a tournament"}")
        print(f"{self._ui.L_LINE}{self._ui.RESET}")
        print("Press q/Q to quit at any time")
        print()

        #name
        state = False
        while state == False:
            name = input("Name: ")
            try:
                state = self._logic.validate_tournament_name(name)
            except EmptyInput:
                print("Tournament needs a name")
            except BackButton:
                return
            
        #Id
        state = False
        while state == False:
            id = input("Tournament id: ")
            try:
                state = self._logic.validate_tournament_id(id)
            except EmptyInput:
                print("Tournament needs an id")
            except IdAlreadyExists:
                print("Id already exists")
            except BackButton:
                return
            

        #Start and End date
        state = False
        while state == False:
            start_date = input("Start date: in the format (day-month-year): ")
            end_date = input("End date: in the format (day-month-year): ")
            try:
                state = self._logic.validate_start_date_and_end_date(start_date, end_date)
            except EmptyInput:
                print("Tournament needs to have a start date and an end date")
            except InvalidStartDateInPast:
                print("Start date is in the past")
            except InvalidStartDateBefore:
                print("End date is before start date")
            except InvalidAmountOfDays:
                print("Tournament has to be between 2-7 days")
            except InvalidFormat:
                print('Invalid format, start and end date have to contain "-" and in the format day-month-year')
            except DateDoesNotExistError:
                print("Start or end date does not exist")
            except BackButton:
                return


        #Venue
        state = False
        while state == False:
            venue = input("Venue: ")
            try:
                state = self._logic.validate_tournament_venue(venue)
            except EmptyInput:
                print("Tournament needs to have a venue")
            except BackButton:
                return
        
        #Contract
        state = False
        while state == False:
            contract = input("Contract: ")
            try:
                state = self._logic.validate_torunament_contract(contract)
            except EmptyInput:
                print("Tournament needs to have a contract")
            except BackButton:
                return
        
        #Contact person email
        state = False
        while state == False:
            contact_email = input("Contact persons email: ")
            try:
                state = self._logic.validate_contact_email(contact_email)
            except EmptyInput:
                print("Tournament needs a contact persons email")
            except InvalidContactEmail:
                print("Contact persons email is invalid, try again")
            except BackButton:
                return


        #Contact persons Phone number
        state = False
        while state == False:
            contact_number = "354" + input("Contact persons phone number: +354")
            try:
                state = self._logic.validate_contact_numer(contact_number)
            except EmptyInput:
                print("Tournament needs a contact persons phone number")
            except InvalidContactNumber:
                print("Contact persons phone number is invalid, try again")
            except BackButton:
                return



        #Number of teams
        state = False
        while state == False:
            num_of_teams = input("Number of teams: ")
            try:
                state = self._logic.validate_tournament_number_of_teams(num_of_teams)
            except ValueError:
                print("Number of teams has to be a digit")
            except WrongNumOfTeams:
                print("Tournament can't have less than 16 teams and can't have more than 64 teams")
            except BackButton:
                return
        num_of_teams = int(num_of_teams)  

        #Number of servers
        state = False
        while state == False:
            num_of_servers = input("Number of servers: ")
            try:
                state = self._logic.validate_servers(num_of_servers, num_of_teams)
            except ValueError:
                print("Number of servers has to be a digit")
            except InvalidServers:
                print("Invalid amount of servers\n"
                "For tournament with less than 32 teams: Servers have to be from 2-4\n"
                "For tournament with 32 or more teams: Servers have to be from 4-7")
            except BackButton:
                return

        #Teams in tournament
        teams_in_tournament: list[str] = []    

        for _ in range(num_of_teams):
            
            state = False
            while state == False:
                team_to_tournament = input("Add team to tournament: ")
                try:
                    state = self._logic.validate_teams_in_tournament(team_to_tournament, teams_in_tournament)
                except TeamAlreadyInTournament:
                    print("Team is already in tournament")
                except TeamDoesNotExist:
                    print("Team does not exist")
                except BackButton:
                    return

            teams_in_tournament.append(team_to_tournament) #Adds the team to the list of teams in the tournement after going through validation     



        self._logic.create_tournament(id, name, venue, start_date, end_date, contract, contact_email, contact_number, num_of_servers, teams_in_tournament )
        input("Tournament has been created, press enter to continue")