from validation.player_validation import ValidatePlayer
from logic.player_logic import PlayerLogic
from Error.player_error import *
from validation.tournament_validation import ValidateTournament
from logic.tournament_logic import TournamentLogic
from Error.tournament_error import *


class OrganizerUI:
    def __init__(self):
        self.validate_player = ValidatePlayer()  
        self.validate_tournament = ValidateTournament()
        self.player_logic = PlayerLogic()  
        self.tournament_logic = TournamentLogic()
        
    def __str__(self):
        return (
            "Organiser\n\n"
            "1. View Teams\n"
            "2. See Tournament\n"
            "3. See match schedule\n"
            "4. Create a player\n"
            "5. Create a tournament\n"
            "6. Create a club\n\n"
            "9. Change role\n\n"
        )

    def get_choice(self):
        """Ask user and return a validated choice."""
        while True:
            print(self)
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "5", "6" "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")
    
        

     
   

    def create_player(self):
        '''Creating a player by asking one information at a time and checking it in Validate Player class'''

        #Name
        state = False 
        while state == False: 
            name = input("Name: ") 
            try: 
                state = self.validate_player.validate_name(name) 

            except EmptyInput: 
                print("Player needs to have a name") 

            


        #Age
        state = False 
        while state == False: 
            age = input("Age: ") 
            try: 
                state = self.validate_player.validate_age(age) 
            except EmptyInput:
                print("Player needs to have an age")
            except WrongAgeException: 
                print("Age has to be a number") 
            except InvalidAgeException: 
                print("Player is too old or too young") 

        #Home address 

        state = False 
        while state == False: 
            address = input("Address: ") 
            try: 
                state = self.validate_player.validate_home_adress(address) 
            except EmptyInput: 
                print("Player needs a home address") 
        

        #Phone 

        state = False 
        while state == False: 
            number = "354" + input("Phone number: +354 ") 
            try: 
                state = self.validate_player.validate_number(number) 
            except EmptyInput: 
                print("Player needs a phone number") 
            except invalidNumberException: 
                print("Number is invalid, try again") 


        #Email 

        state = False 
        while state == False: 
            email = input("Email: ") 
            try: 
                state = self.validate_player.validate_email(email) 
            except EmptyInput: 
                print("Player needs to have an email") 
            except InvalidEmailException: 
                print("Email is invalid, try again") 
        

        #Link 

        state = False 
        while state == False: 
            link = "https://" + input("Link: https://") 
            try: 
                state = self.validate_player.validate_link(link) 
            except EmptyInput: 
                print("Player neeeds to have a link") 
            except InvaldlinkException:
                print("Link has to contain a dot")



        #Handle 

        state = False 
        while state == False: 
            handle = input("Handle: ") 
            try: 
                state = self.validate_player.validate_handle(handle) 
            except EmptyInput: 
                print("Player needs to have a handle") 
            except InvalidCharacterHandle: 
                print("Handle is invalid, try again") 
            except HandleExistsException: 
                print("Handle already exists") 

        self.player_logic.create_player(name, age, address, number, email, link, handle)







        #Tournamnet

    def create_tournoment(self):
        '''Organizer gets asked for information one by one and then information gets sent to logic layer'''
        #name
        state = False
        while state == False:
            name = input("Name: ")
            try:
                state = self.validate_tournament.validate_name(name)
            except EmptyInput:
                print("Tournament needs a name")
            
        #Id
        state = False
        while state == False:
            id = ("Tournament id: ")
            try:
                state = self.validate_tournament.validate_id(id)
            except EmptyInput:
                print("Tournament needs an id")
            except IdAlreadyExists:
                print("Id already exists")
            




        
        #Start and End date
        state = False
        while state == False:
            start_date = input("Start date: ")
            end_date = input("End date: ")
            try:
                state = self.validate_tournament.validate_start_date_and_end_date(start_date, end_date)
            except EmptyInput:
                print("Tournament needs to have a start date and an end date")
            except InvalidStartDateInPast:
                print("Start date is in the past")
            except InvalidStartDateBefore:
                print("Start date is before end date")
        
        

        #Venue
        state = False
        while state == False:
            venue = input("Venue: ")
            try:
                state = self.validate_tournament.validate_venue(venue)
            except EmptyInput:
                print("Tournament needs to have a venue")
            
        
        #Contract
        state = False
        while state == False:
            contract = input("Contract: ")
            try:
                state = self.validate_tournament.validate_contract(contract)
            except EmptyInput:
                print("Tournament needs to have a contract")
            
        
        #Contact person email
        state = False
        while state == False:
            contact_email = input("Contact persons email: ")
            try:
                self.validate_tournament.validate_contact_email(contact_email)
            except EmptyInput:
                print("Tournament needs a contact persons email")
            except InvalidContactEmail:
                print("Contact persons email is invalid, try again")

        #Contact persons Phone number
        state = False
        while state == False:
            contact_number = "354" + input("Contact persons phone number: +354")
            try:
                self.validate_tournament.validate_contact_numer(number)
            except EmptyInput:
                print("Tournament needs a contact persons phone number")
            except InvalidContactNumber:
                print("Contact persons phone number is invalid, try again")
            

        #Number of servers
        state = False
        while state == False:
            num_of_servers = ("Number of servers: ")
            try:
                state = self.validate_tournament.validate_servers(num_of_servers)
            except ValueError:
                print("Number of servers has to be a digit")
            except InvalidServers:
                print("Servers have to be between 1-9")



        #Number of teams
        state = False
        while state == False:
            num_of_teams = input("Number of teams: ")
            try:
                state = self.validate_tournament.validate_number_of_teams(num_of_teams)
            except WrongNumOfTeams:
                print("Tournament can't have less than 16 teams and can't have more than 64 teams")

        #Teams in tournament
               
        for _ in range(num_of_teams):
            teams_in_tournament = []
            
            state = False
            while state == False:
                team_to_tournament = input("Add team to tournament: ")
                try:
                    state = self.validate_tournament.validate_teams_in_tournament(team_to_tournament, teams_in_tournament)
                except TeamAlreadyInTournament:
                    print("Team is already in tournament")
                except TeamDoesNotExist:
                    print("Team does not exist")

            teams_in_tournament.append(team_to_tournament) #Adds the team to the list of teams in the tournement after going through validation     



        self.tournament_logic.create_tournaments(id, name, start_date, end_date, venue, contract, contact_email, contact_number, num_of_servers, teams_in_tournament )


                    






















        