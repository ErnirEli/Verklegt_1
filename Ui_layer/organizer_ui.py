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

    def __str__(self):
        return (
            "Organiser\n\n"
            "1. Player settings\n"
            "2. Team menu\n"
            "3. Club menu\n"
            "4. Tournament menu\n"
            "9. Change role\n\n"
        ) 
      

    def get_choice(self):
        """Ask user and return a validated choice."""
        while True:
            print(self)
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")
    
    #Player
    def player_settings(self) -> str:
        print(
            "Player settings: \n\n"
            "1. Create a Player\n"
            "2. Edit a Player\n"
            "3. See all players\n"
            "4. See player info\n"
            "9. Go back\n\n"
        )
        while True:
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "9"}:
                return choice
        
            print("Invalid choice. Try again.\n\n")
            print(
            "Player settings: \n\n"
            "1. Create a Player\n"
            "2. Edit a Player\n"
            "3. See all players\n"
            "4. See player info\n"
            "9. Go back\n\n")

    def create_player(self):
        '''Creating a player by asking one information at a time and checking it in Validate Player class'''

        print("You are creating a player")
        print("Press q/Q to quit at anytime")

        #Name
        state = False 
        while state == False: 
            name = input("Name: ")            
            try: 
                state = self.validate_player.validate_name(name) 

            except EmptyInput: 
                print("Player needs to have a name") 
            except BackButton:
                return self.player_settings()
            


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
            except BackButton:
                return self.player_settings()



        #Home address 
        state = False 
        while state == False: 
            address = input("Address: ") 
            try: 
                state = self.validate_player.validate_home_adress(address) 
            except EmptyInput: 
                print("Player needs a home address") 
            except BackButton:
                return self.player_settings()

        #Phone 

        state = False 
        while state == False: 
            number = "354" + input("Phone number: +354 ") 
            try: 
                state = self.validate_player.validate_number(number) 
            except EmptyInput: 
                print("Player needs a phone number") 
            except InvalidNumberError: 
                print("Number is invalid, try again")
            except BackButton:
                return self.player_settings() 


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
            except BackButton:
                return self.player_settings()


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
            except BackButton:
                return self.player_settings()
            


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
            except BackButton:
                return self.player_settings()

        self.player_logic.create_player(name, dob, address, number, email, link, handle)
        print("You successfully created a player")
        return self.player_settings() #Returns back to the player settings menu


    def edit_player_info(self):
     
        state = False
        while state == False:
            handle = input("Please provide the handle of the player you want to modify (q/q to quit): ").strip()
            if handle.lower() == "q":
                return self.player_settings #Go back if user wants
            try:
                state = self.validate_player.does_player_exists(handle)
            except PlayerNotExist:
                print("Player does not exist")

        player = self.player_logic.get_full_player_info(handle)
       
        print()
        print("--- Current player info ---")
        for key, value in player.items():
            print(f"  {key}: {value}")

        print("\nLeave edit inputs empty if you don't want to change them.\n")

        #New phone
        while True:
            raw_phone = "354" + input("New phone (empty to keep current): +354").strip()
            if raw_phone == "354":
                new_phone = None
                break

            try:
                self.validate_player.validate_number(raw_phone)
                new_phone = "354" + raw_phone
                break

            except InvalidNumberError:
                print("Number is invalid, try again.")
        

        #New email
        while True:
            raw_email = input("New email (empty to keep current): ")
            if raw_email == "":
                new_email = None
                break

            try:
                self.validate_player.validate_email(raw_email)
                new_email = raw_email
                break
            except InvalidEmailException:
                print("Email is invalid, try again.")

        #New address
        raw_address = input("New address (empty to keep current): ")
        if raw_address == "":
            new_address = None
        else:
            new_address = raw_address

        #New link
        while True:
            raw_link = input("New link: https://")
            if raw_link == "":
                new_link = None
                break

            try:
                self.validate_player.validate_link(raw_link)
                new_link = "https://" + raw_link
                break

            except InvalidLinkException:
                print("Link is invalid, try again (must start with https:// and contain a dot).")

        state = self.player_logic.edit_player_info(
            handle,
            new_phone=new_phone,
            new_email=new_email,
            new_address=new_address,
            new_link=new_link,
        )

        print("Modifications to player info have been made.")
        
        return self.player_settings() #Back to the player settings screen





    def see_all_players(self):
        all_players: list[Player] = self._logic.list_players()
        print("All players:")
        print(f"{"Name":<30}{"Handle":<32}{"Date of birth":<20}{"Team name":<8}")
        for player in all_players:
            print(f"{player.name:<29} {player.handle:<31} {player.dob:<19} {player.team_name:<7}")
      


        go_back = ""
        while go_back.lower() != "q":
            go_back = input("Press q/q to quit")
            
        return self.player_settings()




    def view_player_info(self):
        state = False
        while state == False:
            handle = input("Enter player handle for information (q/Q to quit): ").strip()
            if handle.lower() == "q":
                return self.player_settingsu()
            try:
                state = self.validate_player.does_player_exists(handle)
            except PlayerNotExist:
                print("Player does not exist")
                return self.view_player_info()
        
        player: Player = self._logic.find_player(handle)
           
            
    
        print(f"\n{"-"*29} Player info {"-"*29}")
        print(f"{"Name:":<25} {player.name:>45}")
        print(f"{"Handle:":<25} {player.handle:>45}")
        print(f"{"Team name:":<25} {player.team_name:>45}")
        print(f"{"Date og birht:":<25} {player.dob:>45}")
        print(f"{"Address:":<25} {player.address:>45}")
        print(f"{"Phone number:":<25} {player.phone:>45}")
        print(f"{"Email:":<25} {player.email:>45}")
        print(F"{"Link:":<25} {player.link:>45}")
        print(f"{"Total tournaments played in:":<50} {player.tournament:>20}")
        print(f"{"Tournamnets won:":<25} {player.wins:>45}")
        print()

        return self.player_settings()
    






#------------------------------------------------------------------------------


    #Team
    def team_menu(self) -> str:
        print(
            "Team menu: \n\n"
            "1. create team\n"
            "2. See all teams\n"
            "3. See team info\n"
            "4. Add player to a team\n"
            "5. Remove a player from a team\n"
            "9. Go back\n\n"
        )
        while True:
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "5", "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")

    

    def create_team(self):
        print("You are creating a team")
        print("Press q/Q to quit at any time")
        
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
            except BackButton:
                return self.t()

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
            except BackButton:
                return self.team_menu()
        #ASCII logo
        state = False
        while state == False:
            ascii = input("ASCII logo: ")
            try:
                state = self.validate_team.validate_ascii_logo(ascii)
            except EmptyInput:
                print("Team needs a ASCII logo")
            except BackButton:
                return self.team_menu()
        
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
            except BackButton:
                return self.team_menu()
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
                except BackButton:
                    return self.t()
                
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
            except BackButton:
                return self.team_menu()


        self.team_logic.create_team(name, captain, web_link, ascii, Players_in_team)

    
    def see_all_teams(self):
        all_teams: list[Team] = self._logic.list_teams()
        print("\nAll Teams:")
        print(f"{"Name":<30}{"Club":<15}{"Tournaments Played":^23}{"Wins":<4}")
        for team in all_teams:
            print(f"{team.name:<29} {team.club:<14} {team.tournament:^22} {team.wins:^3}")
       
        go_back = ""
        while go_back.lower() != "q":
            go_back = input("Press q/q to quit")
            
        return self.team_menu()

    
    def see_team_info(self):
        
        state = False
        while state == False:
            name = input("Enter team name for information (q/Q to quit): ").strip()
            if name.lower() == "q":
                return self.team_menu()
            try:
                state = self.validate_team.does_team_exists(name)
            except TeamDoesNotExist:
                print("Team does not exist")
                return self.see_team_info()
       
            players:list[Player] = self._logic.get_team_players(name)#To print players on the bottom

            team: Team = self._logic.get_team(name)
            
        
        
            print(f"\n{self.ui_helper.BOLD}{self.ui_helper.RED}{"-"*30} Team info {"-"*30}{self.ui_helper.RESET}")
            print(f"{"Name:":<25} {team.name:>45}")
            print(f"{"Captain:":<25} {team.captain:>45}")
            print(f"{"Club:":<25} {team.club:>45}")
            print(f"{"Web link:":<10} {team.web_link:>60}")
            print(f"{"ASCII logo:":<25} {team.ASCII:>45}")
            print(f"{"Tournaments Played in:":<25} {team.tournament:>45}")
            print(f"{"Tournaments won:":<25} {team.wins:>45}")
            print(f"{"Total tournaments second places:":<25} {team.runner_up:>38}\n")
            print(f"\n{self.ui_helper.BOLD}{self.ui_helper.RED}{"-"*27} Players in team {"-"*27}{self.ui_helper.RESET}")
            for player in players:
                print(f"{"Name:":<25} {player:>45}")
    
            go_back = ""
            while go_back.lower() != "q":
                go_back = input("Press Q/q to quit")
        return self.team_menu()

    def add_player_to_team(self):
        state = False
        while state == False:
            team_name = input("Enter team name to add players to (q/Q to quit): ")
            if team_name.lower() == "q":
                return self.team_menu()
            try:
                state = self.validate_team.does_team_exists(team_name)
            except TeamExistsError:
                print("Team does not exist")


        players_in_team = self._logic.get_team_players(team_name)
        
        if len(players_in_team) > 5:
            print("Team is full")
            return self.add_player_to_team()
            
        state = False
        while state == False:
            player_name = input("Enter player handle to add to team (q/Q to quit): ")
            try:
                state = self.validate_team.validate_players_in_team(player_name)
            except PlayerDoesNotExistError:
                print("Player does not exist")
            except playerNotAvailableError:
                print("Player is Already in a team")
            except BackButton:
                return self.team_menu()
        
        team: Team = self._logic.get_team(team_name)
        player: Player= self._logic.find_player(player_name)
     
        self._logic.add_player(team, player)
        print("Player has been added to the team")

        return self.team_menu()





    def remove_player_from_team(self):
        state = False
        while state == False:
            team_name = input("Enter team name to remove players from (q/Q to quit): ")
            if team_name.lower() == "q":
                return self.team_menu()
            try:
                state = self.validate_team.does_team_exists(team_name)
            except TeamExistsError:
                print("Team does not exist")
        

        players_in_team: list[Player] = self._logic.get_team_players(team_name)
        
        
        if len(players_in_team) < 4:
            print("There are too few players in the team to remove from it")
            return self.remove_player_from_team() #go back to the top
            
        team: Team = self._logic.get_team(team_name)#Goes in validation to check if captain is removed

        
        while True: 
            player_name = input("Enter player handle to add to team (q/Q to quit): ")
            try:
                self.validate_team.validate_player_to_remove(player_name, team)
                
            except PlayerDoesNotExistError:
                print("Player does not exist")
                continue
            except BackButton:
                return self.team_menu()
            except CantRemoveCaptainError:
                print("Captain can not be removed")
                continue
       

            player: Player= self._logic.find_player(player_name)
            if player.handle not in players_in_team:
                print(player.name)
                print(players_in_team)
                print("player is not in the team")
            else:
                break    
       
        # team: Team = self._logic.get_team(team_name)
        
        # if team.name != player.team_name:
        #     print("Player is not in the team")
        #     return self.remove_player_from_team()
    
    
        self._logic.remove_player(player)
        print("Player has been removed from the team")

        return self.team_menu()

#--------------------------------------------------------------------------
#Club
    def club_menu(self)-> str:
        print(
            "Club menu:\n\n"
            "1. Create a club\n"
            "2. See all clubs\n"
            "3. See club info\n"
            "4. Add team to a club\n"
            "5. Remove team from a club\n"
            "9. Go back\n\n"
        )
        while True:
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "5", "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")

    

    def create_club(self):
        print("You are creating a club")
        print("Press q/Q to quit at any time")
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
            except BackButton:
                return self.club_menu()

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
            except BackButton:
                return self.club_menu()

        #Hometown
        state = False
        while state == False:
            hometown = input("Hometown: ")
            try:
                state = self.validate_club.validate_hometown(hometown)
            except EmptyInput:
                print("Club needs to have a hometown")
            except BackButton:
                return self.club_menu()
        
        #Country
        state = False
        while state == False:
            country = input("Country: ")
            try:
                state = self.validate_club.validate_country(country)
            except EmptyInput:
                print("Club needs to have a country")
            except BackButton:
                return self.club_menu()
            

        #Number of tems in club
        state = False
        while state == False:
            num_of_teams = input("Number of teams in club:")
            try:
                state = self.validate_club.validate_num_of_teams(num_of_teams)
            except ValueError:
                print("Number of teams have to be a digit")
            except InvalidNumOfTeams:
                print("Club can only have 1-5 teams")
            except BackButton:
                return self.club_menu()
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
                except BackButton:
                    return self.club_menu()
            teams_in_club.append(team_to_club)
            



        self.club_logic.create_club(name, color, hometown, country, teams_in_club)
    

    def see_all_clubs(self):
        all_clubs: list[Club] = self._logic.list_clubs()
        print("\nAll Clubs:")
        print(f"{"Name":<30}{"Country":<15}{"Tournaments Played":<23}{"Wins":<4}")
        for club in all_clubs:
            print(f"{club.name:<30}{club.country:<15}{club.tournaments:^23}{club.wins:^4}")
       
        go_back = ""
        while go_back.lower() != "q":
            go_back = input("\nPress q/q to quit")
            
        return self.team_menu()

    def see_club_info(self):
        state = False
        while state == False:
            name = input("Enter club name for information (q/Q to quit): ").strip()
            if name.lower() == "q":
                return self.club_menu()
            try:
                state = self.validate_club.does_club_exist(name)
            except ClubDoesNotExist:
                print("Club does not exist")
                return self.see_club_info()

        club: Club = self._logic.get_club(name)
        teams: list[Team] = self._logic.get_club_teams(club)#To print teams on the bottom
        
        club: Club = self._logic.get_club(name)
    
    
        print(f"\n{self.ui_helper.BOLD}{self.ui_helper.RED}{"-"*30} Team info {"-"*30}{self.ui_helper.RESET}")
        print(f"{"Name:":<25} {club.name:>45}")
        print(f"{"Color:":<25} {club.color:>45}")
        print(f"{"hometown:":<25} {club.hometown:>45}")
        print(f"{"country:":<10} {club.country:>60}")
        print(f"{"Tournaments played in:":<25} {club.tournaments:>45}")
        print(f"{"Total tournaments second places:":<25} {club.runner_up:>38}\n")
        print(f"\n{self.ui_helper.BOLD}{self.ui_helper.RED}{"-"*27} Teams in club {"-"*27}{self.ui_helper.RESET}")
        for team in teams:
            print(f"{"Name:":<25} {team:>45}\n")
        go_back = ""
        while go_back.lower() != "q":
            go_back = input("Press Q/q to quit")
        return self.see_club_info()

    def add_team_to_club(self):
        state = False
        while state == False:
            club_name = input("Enter club name to add teams to (q/Q to quit): ")
            if club_name.lower() == "q":
                return self.club_menu()
            
            try:
                state = self.validate_club.does_club_exist(club_name)
            except ClubDoesNotExist:
                print("Club does not exist")
        
        

        club: Club = self._logic.get_club(club_name)
        teams_in_club: list[Team] = self._logic.get_club_teams(club)
        
        if len(teams_in_club) > 5:
            print("Club is full")
            return self.add_team_to_club()
            
        state = False
        while state == False:
            team_name = input("Enter team name to add to club (q/Q to quit): ")
            try:
                state = self.validate_club.validate_teams_in_club(team_name)
            except TeamDoesNotExistError:
                print("Team does not exist")
            except BackButton:
                return self.team_menu()
            except TeamNotAvailableError:
                print("Team is already in a club")
            

        
        team: Team = self._logic.get_team(team_name)
        

        self._logic.add_team(club, team)
        print("Team added to club")

        return self.team_menu()


    def remove_team_from_club(self):
        state = False
        while state == False:
            club_name = input("Enter club name to remove teams from(q/Q to quit): ")
            if club_name.lower() == "q":
                return self.club_menu()
            
            try:
                state = self.validate_club.does_club_exist(club_name)
            except ClubDoesNotExist:
                print("Club does not exist")
        
        

        club: Club = self._logic.get_club(club_name)
        teams_in_club: list[Team] = self._logic.get_club_teams(club)
        
        if len(teams_in_club) < 2:
            print("The club does not have enough teams to remove one")
            return self.add_team_to_club()
            
        state = False
        while state == False:
            team_name = input("Enter team name to remove from club (q/Q to quit): ")
            if team_name.lower() == "q":
                return self.club_menu()
            try:
                state = self.validate_club.validate_club_to_remove(team_name)
            except TeamDoesNotExistError:
                print("Team does not exist")
            


        
        team: Team = self._logic.get_team(team_name)
        if team.name not in teams_in_club:
            print("Team is not in the Club")
            return self.remove_team_from_club()
       
      
    
        self._logic.remove_team(team)
        print("Player has been removed from the club")

        return self.team_menu()





#---------------------------------------------------

#Tournament
    def tournament_menu(self)-> str:
        print(
            "Tournament menu:\n\n"
            "1. Create a tournament\n"
            "2. See all tournmanets\n"
            "3. See tournament info\n"
            "4. Input match scores\n"
            "9. Go back\n\n"
        )
        while True:
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "6", "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")

    

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

  


                


        














        