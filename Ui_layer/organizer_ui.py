#from logic.logic_api import logicAPI

from Error.general_error import EmptyInput
from Error.general_error import DateDoesNotExistError

#Player imports
from validation.player_validation import ValidatePlayer
from logic.player_logic import PlayerLogic
from Error.player_error import *

#Tournaments imports
from validation.tournament_validation import ValidateTournament
from logic.tournament_logic import TournamentLogic
from Error.tournament_error import *

#team imports
from logic.team_logic import TeamLogic
from validation.team_validation import ValidateTeam
from Error.team_error import *

#Club imports
from logic.club_logic import ClubLogic
from validation.club_validation import ValidateClub
from Error.club_error import *



class OrganizerUI:
    def __init__(self):
        #self._logic = logicAPI()

        self.validate_player = ValidatePlayer()  
        self.player_logic = PlayerLogic()  
        
        self.validate_tournament = ValidateTournament()
        self.tournament_logic = TournamentLogic()
        
        self.validate_team = ValidateTeam()
        self.team_logic = TeamLogic()

        self.validate_club = ValidateClub()
        self.club_logic = ClubLogic()

    def __str__(self):
        return (
            "Organiser\n\n"
            "1. View Teams\n"
            "2. See Tournament\n"
            "3. See match schedule\n"
            "4. Create a player\n"
            "5. Create a tournament\n"
            "6. Create a club\n"
            "7. create a team\n\n"
            "9. Change role\n\n"
        )

    def get_choice(self):
        """Ask user and return a validated choice."""
        while True:
            print(self)
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "5", "6", "7", "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")
    
    
    # def view_teams(self):
    #     return
    
    # def view_player_info(self):
    #     handle = input("Enter player handle: ").strip()
    #     player = self._logic.get_full_player_info(handle)
    #     if player is None:
    #         print("No player found with that handle.")
    #     else:
    #         print("\n--- Player info ---")
    #         print(f"Handle: {player.handle}")
    #         print(f"Team name: {player.team_name}")
    #         print(f"Date og birht: {player.dob}")
    #         print(f"Address: {player.address}")
    #         print(f"Phone number: {player.phone}")
    #         print(f"Email: {player.email}")
    #         print(F"Link: {player.link}")
    #         print(f"Total tournaments played in: {player.tournaments}")
    #         print(f"Tournamnets won: {player.wins}")

     
   

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

            


        #Date of Birth
        state = False 
        while state == False: 
            dob = input("Date of birth: in format(Day-month-year): ") 
            try: 
                state = self.validate_player.validate_age(dob) 
            except EmptyInput:
                print("Player needs to have a date of birth")
            except TooYoungError:
                print("Player is too young") 
            except TooOldError:
                print("Player is too old")
            except InvalidAgeException: 
                print("Date of birth needs to be in the format: day-month-year") 
            except DateDoesNotExistError:
                print("Date does not exist")



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

        self.player_logic.create_player(name, dob, address, number, email, link, handle)







    #     #Tournamnet

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
            id = input("Tournament id: ")
            try:
                state = self.validate_tournament.validate_id(id)
            except EmptyInput:
                print("Tournament needs an id")
            except IdAlreadyExists:
                print("Id already exists")
            




        
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
                state = self.validate_tournament.validate_contact_email(contact_email)
            except EmptyInput:
                print("Tournament needs a contact persons email")
            except InvalidContactEmail:
                print("Contact persons email is invalid, try again")

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
            

        #Number of servers
        state = False
        while state == False:
            num_of_servers = input("Number of servers: ")
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
            except ValueError:
                print("Number of teams has to be a digit")

            except WrongNumOfTeams:
                print("Tournament can't have less than 16 teams and can't have more than 64 teams")

        #Teams in tournament
        num_of_teams = int(num_of_teams)      
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



        self.tournament_logic.create_a_tournament(id, name, venue, start_date, end_date, contract, contact_email, contact_number, num_of_servers, teams_in_tournament )




    def create_team(self):
        #Name
        state = False
        while state == False:
            name = input("Name: ")
            try:
                state = self.validate_team.validate_name(name)
            except EmptyInput:
                print("Team needs to have a name")
            except TeamExistsError:
                print("Team name already exit, team needs an unique name")
            

        # Web link
        state = False
        while state == False:
            web_link = "https://" + input("Web link: https://")
            try:
                state = self.validate_team.validate_web_link(web_link)
            except EmptyInput:
                print("Team needs to have a web link")
            except InvalidWebLink:
                print("Web link needs to contain a dot")
        
        #ASCII logo
        state = False
        while state == False:
            ascii = input("ASCII logo: ")
            try:
                state = self.validate_team.validate_ascii_logo(ascii)
            except EmptyInput:
                print("Team needs a ASCII logo")
        
        #Number of players in team
        #3-5
        state = False
        while state == False:
            num_of_players = input("Number of players in team: ")
            try:
                state = self.validate_team.validate_number_of_players(num_of_players)
            except ValueError:
                print("Number of players has to be a digit")

            except EmptyInput:
                print("Team must have 3-5 players")
            except TooManyPlayersError:
                print("Team can not have more than 5 players")
            except NotEnoughPlayersError:
                print("Team needs to have at least 3 players")
        int(num_of_players)
            

        #Players in team
        num_of_players = int(num_of_players)
        Players_in_team = []
        for _ in range(num_of_players):
            state = False
            while state == False:
                player_handle = input("Player handle to add to team: ")
                try:
                    state = self.validate_team.validate_players_in_team(player_handle, Players_in_team)
                except PlayerDoesNotExistError:
                    print("Player does not exist")
                except PlayerAlreadyInTeamError:
                    print("Player already in Team")
                except playerNotAvailableError:
                    print("Player is already in an another team")

            Players_in_team.append(player_handle)

        #captain
        state = False
        while state == False:
            captain = input("Choose a captain (handle): ")
            try:
                state = self.validate_team.validate_captain(captain, Players_in_team)
            except EmptyInput:
                print("Team needs a captain")
            except CaptainNotExistError:
                print("Player does not exist")
            except CaptainNotInTeamError:
                print("Captain is not in the team")


        self.team_logic.create_team(name, captain, web_link, ascii, num_of_players, Players_in_team)







    def create_club(self):

        #name
        state = False
        while state == False:
            name = input("Name: ")
            try:
                state = self.validate_club.name_validation(name)
            except EmptyInput:
                print("Club needs to have a name")
            except ClubNameExistsError:
                print("Name already exissts, club needs to have an unique name")


        #Colors
        state = False
        print("Available colors: [blue, light blue, red, light red, orange, green, light green, yellow, black, white, brown, purple, light purple, cyan, light cyan, light gray, dark gray]")
        while state == False:
            color = input("Choose 1 color: ")
            try:
                state = self.validate_club.validate_colors(color)
            except EmptyInput:
                print("Club needs to have at least one color")
            except ColorNotAvailable:
                print("Color not available")

        #Hometown
        state = False
        while state == False:
            hometown = input("Hometown: ")
            try:
                state = self.validate_club.validate_hometown(hometown)
            except EmptyInput:
                print("Club needs to have a hometown")
        
        #Country
        state = False
        while state == False:
            country = input("Country: ")
            try:
                state = self.validate_club.validate_country(country)
            except EmptyInput:
                print("Club needs to have a country")
            

        #Number of tems in club
        state = False
        while state == False:
            num_of_teams = input("Number of teams in club:")
            try:
                state = self.validate_club.validate_num_of_teams(num_of_teams)
            except ValueError:
                print("Number of teams have to be a digit")
            except InvalidNumOfTeams:
                print("Club can only have 1-10 teams")
        num_of_teams = int(num_of_teams)
        
        
        
        

        #Teams in club
        teams_in_club = []
        for _ in range(num_of_teams):
            
            
            state = False
            while state == False:
                team_to_club = input("Team in club: ")
                try:
                    state = self.validate_club.validate_teams_in_club(team_to_club, teams_in_club)
                except TeamDoesNotExistError:
                    print("Team does not exist")
                except TeamAlreadyInClubError:
                    print("Team is already in the club")
                except TeamNotAvailableError:
                    print("Team is already in an another club")
            teams_in_club.append(team_to_club)
            



        self.club_logic.create_club(name, color, hometown, country, teams_in_club)
        return











        