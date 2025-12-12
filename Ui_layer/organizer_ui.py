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



class OrganizerUI:
    def __init__(self):
        self._logic = LogicAPI()
        self.ui_helper = UIHelper()

        self.validate_player = ValidatePlayer()  
        self.player_logic = PlayerLogic()  
        
        self.validate_tournament = ValidateTournament()
        self.tournament_logic = TournamentLogic()
        
        self.validate_team = ValidateTeam()
        self.team_logic = TeamLogic()

        self.validate_club = ValidateClub()
        self.club_logic = ClubLogic()

        self.validate_match = ValidateMatch()

    
#---------------------------------------------------
    def create_tournoment(self):
        '''Organizer gets asked for information one by one and then information gets sent to logic layer'''
        print("You are creating a Tournament")
        print("Press q/Q to quit at any time")

        #name
        state = False
        while state == False:
            name = input("Name: ")
            try:
                state = self.validate_tournament.validate_name(name)
            except EmptyInput:
                print("Tournament needs a name")
            except BackButton:
                return self.tournament_menu()
            
        #Id
        state = False
        while state == False:
            id = input("Tournament id: ")
            try:
                state = self.validate_tournament.validate_id(id)
            except EmptyInput:
                print("Tournament needs an id")
            except IdAlreadyExists:
                print("Id already exists")
            except BackButton:
                return self.tournament_menu()
            




        
        #Start and End date
        state = False
        while state == False:
            start_date = input("Start date: in the format (day-month-year): ")
            end_date = input("End date: in the format (day-month-year): ")
            try:
                state = self.validate_tournament.validate_start_date_and_end_date(start_date, end_date)
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
                return self.tournament_menu()


        #Venue
        state = False
        while state == False:
            venue = input("Venue: ")
            try:
                state = self.validate_tournament.validate_venue(venue)
            except EmptyInput:
                print("Tournament needs to have a venue")
            except BackButton:
                return self.tournament_menu()
        
        #Contract
        state = False
        while state == False:
            contract = input("Contract: ")
            try:
                state = self.validate_tournament.validate_contract(contract)
            except EmptyInput:
                print("Tournament needs to have a contract")
            except BackButton:
                return self.tournament_menu()
        
        #Contact person email
        state = False
        while state == False:
            contact_email = input("Contact persons email: ")
            try:
                state = self.validate_tournament.validate_contact_email(contact_email)
            except EmptyInput:
                print("Tournament needs a contact persons email")
            except InvalidContactEmail:
                print("Contact persons email is invalid, try again")
            except BackButton:
                return self.tournament_menu()


        #Contact persons Phone number
        state = False
        while state == False:
            contact_number = "354" + input("Contact persons phone number: +354")
            try:
                state = self.validate_tournament.validate_contact_numer(contact_number)
            except EmptyInput:
                print("Tournament needs a contact persons phone number")
            except InvalidContactNumber:
                print("Contact persons phone number is invalid, try again")
            except BackButton:
                return self.tournament_menu()



        #Number of teams
        state = False
        while state == False:
            num_of_teams = input("Number of teams: ")
            try:
                state = self.validate_tournament.validate_number_of_teams(num_of_teams)
            except ValueError:
                print("Number of teams has to be a digit")
            except WrongNumOfTeams:
                print("Tournament can't have less than 16 teams and can't have more than 64 teams")
            except BackButton:
                return self.tournament_menu()
        num_of_teams = int(num_of_teams)  

        #Number of servers
        state = False
        while state == False:
            num_of_servers = input("Number of servers: ")
            try:
                state = self.validate_tournament.validate_servers(num_of_servers, num_of_teams)
            except ValueError:
                print("Number of servers has to be a digit")
            except InvalidServers:
                print("Invalid amount of servers\n"
                "For tournament with less than 32 teams: Servers have to be from 2-4\n"
                "For tournament with 32 or more teams: Servers have to be from 4-7")
            except BackButton:
                return self.tournament_menu()

        #Teams in tournament
        teams_in_tournament = []    
        for _ in range(num_of_teams):
            
            
            state = False
            while state == False:
                team_to_tournament = input("Add team to tournament: ")
                try:
                    state = self.validate_tournament.validate_teams_in_tournament(team_to_tournament, teams_in_tournament)
                except TeamAlreadyInTournament:
                    print("Team is already in tournament")
                except TeamDoesNotExist:
                    print("Team does not exist")
                except BackButton:
                    return self.tournament_menu()

            teams_in_tournament.append(team_to_tournament) #Adds the team to the list of teams in the tournement after going through validation     



        self.tournament_logic.create_tournament(id, name, venue, start_date, end_date, contract, contact_email, contact_number, num_of_servers, teams_in_tournament )

    def see_all_tournaments(self):
        all_tournaments: list[Tournament] = self._logic.list_tournaments()
        print("\nAll Tournamnets:")
        print(f"{"Name":<60}{"ID":<18}{"State":<15}")
        for tournament in all_tournaments:
            print(f"{tournament.name:<60}{tournament.id:<18}{str(tournament.state):<15}")
            
        go_back = ""
        while go_back.lower() != "q":
            go_back = input("\nPress Q/q to quit")
            
        return self.team_menu()

    def see_tournament_info(self):
        state = False
        while state == False:
            id = input("Enter Tournament ID for information (q/Q to quit): ").strip()
            if id.lower() == "q":
                return self.tournament_menu()
            try:
                state = self.validate_tournament.does_tournament_id_exist(id)
            except TournamentNotExistError:
                print("Tournament does not exist")
                return self.see_tournament_info()

        tournament: Tournament = self._logic.get_tournament(id)
        
        
        print(f"\n{self.ui_helper.BOLD}{self.ui_helper.RED}{"-"*27} Tournament info {"-"*27}{self.ui_helper.RESET}")
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
        
        print(f"\n{self.ui_helper.BOLD}{self.ui_helper.RED}{"-"*24} Matches in tournament {"-"*24}{self.ui_helper.RESET}")
            
        all_matches: list[Match] = self._logic.list_matches()
      
        for match in all_matches:
            if match.tournament_id == id:
                print(match)

        go_back = ""
        while go_back.lower() != "q":
            go_back =input("\nPress Q/q to quit")
        return self.tournament_menu()

    def input_match_scores(self):

        
        state = False
        while state == False:
            id = input("Enter Tournament ID for inputin match results (q/Q to quit): ").strip()
            if id.lower() == "q":
                return self.tournament_menu()
            try:
                state = self.validate_tournament.does_tournament_id_exist(id)
            except TournamentNotExistError:
                print("Tournament does not exist")
                return self.input_match_scores()
        

        back_button = ""
        while back_button.lower() != "q":
        
            tournament: Tournament = self._logic.get_tournament(id)
            if tournament.state == True:
                print("Tournament is finished")
                return self. input_match_scores()
            
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
                        state = self.validate_match.validate_score(a_score, b_score)
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
            
        return self.tournament_menu()

  


                


        














        