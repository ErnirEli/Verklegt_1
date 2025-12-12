# Models
from models.team import Team
from models.tournament  import Tournament
from models.match import Match
from models.club import Club
from models.player import Player

# Logic
from logic.team_logic import TeamLogic
from logic.tournament_logic import TournamentLogic
from logic.match_logic import MatchLogic
from logic.club_logic import ClubLogic
from logic.player_logic import PlayerLogic
from logic.schedule_logic import ScheduleLogic

# Validations
from validation.player_validation import ValidatePlayer
from validation.team_validation import ValidateTeam
from validation.club_validation import ValidateClub
from validation.tournament_validation import ValidateTournament
from validation.match_validation import ValidateMatch


class LogicAPI:

    def __init__(self) -> None:
        self._team_logic = TeamLogic()
        self._tournament_logic = TournamentLogic()
        self._match_logic = MatchLogic()
        self._club_logic = ClubLogic()
        self._player_logic = PlayerLogic()
        self._schedule_logic = ScheduleLogic()
        self._player_validation = ValidatePlayer()
        self._team_validation = ValidateTeam()
        self._club_validation = ValidateClub()
        self._tournament_validation = ValidateTournament()
        self._match_validation = ValidateMatch()

# Logic

    # Teams

    def list_teams(self) -> list[Team]:
        '''Takes in nothing and returns a list of all existing teams of type Team'''

        return self._team_logic.list_all_teams()
    
    def create_team(self, name: str, captain: str, web_link: str, ASCII: str, players: list[str]) -> Team:
        '''Takes in a name, captain handle, web link, ASCII all of string type,
        also takes in a list of player handles of type string. 
        Creates a team and adds players to the team.
        Returns the team of type Team
        Only runs after all validation checks are valid.'''

        return self._team_logic.create_team(name, captain, web_link, ASCII, players)
    
    def add_player(self, team: Team, player: Player) -> None:
        '''Takes in a team, of type Team, and
        a player of type Player,
        adds the player to the team.
        Only runs after all validation checks are valid.'''

        self._team_logic.add_player(team, player)
        return
    
    def remove_player(self, player: Player) -> None:
        '''Takes in a player, of type Player, 
        and removes him from team.
        Only runs after all validation checks are valid.'''

        self._team_logic.remove_player(player)
        return

    def get_team(self, team_name: str) -> Team:
        '''Takes in a team name as a string,
        finds the team with the right name and
        returns it of type Team.
        Only runs after all validation checks are valid.'''

        return self._team_logic.get_team(team_name)
    
    def get_team_players(self, name: str) -> list[Player]:
        '''Takes in a team name of type string, returns a list of all players in the team, of type Player'''

        return self._team_logic.get_team_players(name)

    # Tournaments

    def list_tournaments(self) -> list[Tournament]:
        '''Takes in nothing and returns a list of all existing tournaments of type Tournament'''

        return self._tournament_logic.list_all_tournaments()
    
    def get_tournament(self, tournament_id: str) -> Tournament:
        '''Takes in tournament ID and returns the torunament of type Torunament.
        Only runs after all validation checks are valid.'''

        return self._tournament_logic.get_tournament(tournament_id)

    def create_tournament(self, tournament_id: str, name: str, venue: str,
                        start_date: str, end_date: str, contact: str, contact_email: str,
                        contact_number: str, servers: int, team_list: list[str]) -> Tournament:
        '''Takes in id, name, venue, start & end dates, contact, mail & number, servers, for a tournament, all of type string.
        also takes in a list of team names of type string. Creates a tournament using this info and adds all teams from the list to the torunament.
        Only runs after all validation checks are valid.'''

        return self._tournament_logic.create_tournament(tournament_id, name, venue, end_date, start_date,
                                                        contact, contact_email, contact_number, servers, team_list)
    
    # Matches
    
    def list_matches(self) -> list[Match]:
        '''Takes in nothing and returns a list of all existing amtches of type Match'''

        return self._match_logic.list_all_matches()
    
    def update_game_results(self, match: Match, score_a: int, score_b: int) -> None:
        '''Takes in a match of type "Match" and score for team a & b.
        Updates match winner and status and finishes the tournament if match round in "Final".
        Returns None
        Only runs after all validation checks are valid.'''

        self._match_logic.update_game_results(match, score_a, score_b)
        return


    # Clubs

    def list_clubs(self) -> list[Club]:
        '''Takes in nothing and returns a list of all existing clubs of type Club'''

        return self._club_logic.list_all_clubs()
    
    def create_club(self, name: str, color: str, hometown: str, country: str, teams: list[str]) -> None:
        '''Takes in a name, color, hometown, country all of type string, also takes in a list of team names, of type string.
        Creates a club of type "Club" and adds all teams from list to the club. Returns None.
        Only runs after all validation checks are valid.'''

        return self._club_logic.create_club(name, color, hometown, country, teams)

    def get_club_teams(self, club: Club) -> list[Team]:
        '''Takes in a club of type Club and returns a list of all teams in the club, of type "Team".
        Only runs after all validation checks are Valid'''

        return self._club_logic.get_club_teams(club)

    def add_team(self, club: Club, team: Team) -> None:
        '''Takes in a club, og type "Club" and a team of type Team.
        adds team tou the club.
        Only runs after all validation checks are valid'''

        self._club_logic.add_team(club, team)
        return
        
    def remove_team(self, team: Team) -> None:
        '''Takes in a team of type "Team" and removes it from club.
        Only runs after ale validation checks are valid.'''

        self._club_logic.remove_team(team)
        return

    def get_club(self, club_name: str) -> Club:
        '''Takes in club name of type string and returns club of type Club.
        Only runs after ale validation checks are valid.'''

        return self._club_logic.get_club(club_name)


    # Player

    def create_player(self, name: str, dob: str, address: str, phone: str, email: str,
                    link: str, handle: str) -> None:
        '''Takes in name, date of birth, adress, phone number, email, link, and hadle.
        Creates a player of type "Club" and saves him in the player CSV file.
        Only runs after all Validation checks are valid'''

        self._player_logic.create_player(name, dob, address, phone, email, link, handle)
        return
    
    def find_player(self, handle: str) -> Player:
        '''Takes in a player handle of type string.
        Returns the player with same handle of type "Player".
        Only runs after all Validation checks are valid.'''

        return self._player_logic.find_player(handle)

    def edit_player_info(self, handle: str, new_phone = None,  new_email = None, new_address = None, new_link = None) -> Player:
        '''Takes in a player handle and 1-4 of the following arguments: 
        phone number, email, address, link and changes the info for the player.
        Only runs if all Validation checks are valid.'''
        
        return self._player_logic.edit_player_info(handle, new_phone = new_phone, new_email = new_email, new_address = new_address, new_link=new_link)
    
    def list_players(self) -> list[Player]:
        '''Takes in nothing and returns a list of all players'''

        return self._player_logic.get_all_players()
    

    #Schedule
    def get_active_matches(self, tournament) -> list[Match]:
        '''Takes in a tournament of type Tournament and returns a list of all matches in active round'''

        return self._schedule_logic.get_active_matches(tournament)


# Validations   

    # Player

    def validate_player_name(self, name: str) -> bool:
        '''Takes a player name of type string and checks if it is valid,
        Raises an error if name is invalid'''

        return self._player_validation.validate_name(name)
    
    def validate_player_age(self, dob: str) -> bool: 
        '''Takes a player date of birth of type string and checks if it is valid form and if player is 18 years old,
        Raises an error if date of birth or age is invalid'''

        return self._player_validation.validate_age(dob)

    def validate_player_address(self, address: str) -> bool:
        '''Takes a player adress of type string and checks if it is valid form. 
        Raises an error if adress is invalid'''

        return self._player_validation.validate_home_address(address)
    
    def validate_player_email(self, email: str) -> bool:
        '''Takes a player email of type string and checks if it is valid form. 
        Raises an error if eamil is invalid'''

        return self._player_validation.validate_email(email)
    
    def validate_player_number(self, number: str) -> bool:
        '''Takes a player number of type string and checks if it is valid form. 
        Raises an error if number is invalid'''

        return self._player_validation.validate_number(number)
    
    def validate_player_link(self, link: str) -> bool:
        '''Takes a player link of type string and checks if it is valid form. 
        Raises an error if link is invalid'''

        return self._player_validation.validate_link(link)
    
    def validate_player_handle(self, handle: str) -> bool:
        '''Takes a player handle of type string and checks if it is valid form. 
        Raises an error if handle is invalid'''

        return self._player_validation.validate_handle(handle)

    def does_player_exists(self, handle: str) -> bool:
        '''Takes a player handle of type string and checks if player exists. 
        Raises an error if handle is invalid'''

        return self._player_validation.does_player_exists(handle)
    

    # Club

    def validate_club_name(self, name: str) -> bool:
        '''Takes a club name of type string and checks if it is valid,
        Raises an error if name is invalid'''

        return self._club_validation.name_validation(name)

    def validate_club_colors(self, color: str) -> bool:
        '''Takes a club color of type string and checks if it is valid,
        Raises an error if color is invalid'''

        return self._club_validation.validate_colors(color)
    
    def validate_club_hometown(self, hometown: str) -> bool:
        '''Takes a club hometown of type string and checks if it is valid,
        Raises an error if hometown is invalid'''

        return self._club_validation.validate_hometown(hometown)
    
    def validate_club_country(self, country: str) -> bool:
        '''Takes a club country of type string and checks if it is valid,
        Raises an error if country is invalid'''

        return self._club_validation.validate_country(country)
    
    def validate_num_of_teams(self, num_of_teams: str) -> bool:
        '''Takes number of teams for a club of type string and checks if it is valid,
        Raises an error if number of teams is invalid'''

        return self._club_validation.validate_num_of_teams(num_of_teams)
    
    def validate_teams_in_club(self, team_to_club: str, teams_in_club: list) -> bool:
        '''Takes a team name for club of type string and a list of teams already in club, checks if team is already in club,
        Raises an error if team is already in the club'''

        return self._club_validation.validate_teams_in_club(team_to_club, teams_in_club)
    
    def does_club_exist(self, club_name: str) -> bool:
        '''Takes in a club of string type and validates if it exists.
        Raises an ClubDoesNotExist if club does not exist.'''

        return self._club_validation.does_club_exist(club_name)

    def validate_club_to_remove(self, team_name: str) -> bool:
        '''Takes in a team name an validates if it is alowed to be removed from club.
        Raises an error if it is not valid.'''

        return self._club_validation.validate_club_to_remove(team_name)
    # Teams

    def validate_team_name(self, name: str) -> bool:
        '''Takes team name of type string and checks if it is valid,
        Raises an error if name of teams is invalid'''

        return self._team_validation.validate_name(name)
    
    def validate_team_captain(self, captain: str, players_in_team: list) -> bool:
        '''Takes team captain handle of type string and a list of players in team, checks if captain is valid,
        Raises an error if captain is invalid'''

        return self._team_validation.validate_captain(captain, players_in_team)
    
    def validate_team_web_link(self, web_link: str) -> bool:
        '''Takes team link of type string and checks if it is valid,
        Raises an error if link is invalid'''

        return self._team_validation.validate_web_link(web_link)
    
    def validate_team_ascii_logo(self, ascii: str) -> bool:
        '''Takes team logo of type string and checks if it is valid,
        Raises an error if logo is invalid'''

        return self._team_validation.validate_ascii_logo(ascii)
    
    def validate_number_of_players(self, num_of_players: str) -> bool:
        '''Takes number of players in team of type string and checks if it is valid,
        Raises an error if number of players is invalid'''

        return self._team_validation.validate_number_of_players(num_of_players)
    
    def validate_players_in_team(self, player_to_team: str, players_in_team: list[str]) -> bool:
        '''Takes in a player name of type string and a list of players already in the team, of type string.
        checks if player is already in team.
        raises error of player is already in team.'''

        return self._team_validation.validate_players_in_team(player_to_team, players_in_team)
    
    def does_team_exists(self, name: str) -> bool:
        '''Takes in team name of type string and checks if a team with that name exists.
        raises an error if no team is found'''

        return self._team_validation.does_team_exists(name)
    
    def validate_player_to_remove(self, player_handle: str, team: Team):
        '''Takes in player handle of type str and a team of type Team.
        Raises an error if player can not be removed'''

        return self._team_validation.validate_player_to_remove(player_handle, team)
    

    # Tournament

    def validate_tournament_name(self, name: str) -> bool:
        '''Takes tournament name of type string and checks if it is valid,
        Raises an error if name is invalid'''

        return self._tournament_validation.validate_name(name)
    
    def validate_start_date_and_end_date(self, start_date: str, end_date: str) -> bool:
        '''Takes tournament start and end date of type string and checks if it is valid,
        checks if is a valid foramt and if tournament ends bofore starting.
        Raises an error if name is invalid'''

        return self._tournament_validation.validate_start_date_and_end_date(start_date, end_date)

    def validate_tournament_venue(self, venue: str) -> bool:
        '''Takes tournament venue of type string and checks if it is valid,
        Raises an error if venue is invalid'''

        return self._tournament_validation.validate_venue(venue)
    
    def validate_torunament_contract(self, contract: str) -> bool:
        '''Takes tournament contact of type string and checks if it is valid,
        Raises an error if contact is invalid'''

        return self._tournament_validation.validate_contract(contract)
    
    def validate_contact_email(self, email: str) -> bool:
        '''Takes tournament contact email of type string and checks if it is valid,
        Raises an error if contact email is invalid'''

        return self._tournament_validation.validate_contact_email(email)
    
    def validate_contact_numer(self, number: str) -> bool:
        '''Takes tournament contact number of type string and checks if it is valid,
        Raises an error if contact number is invalid'''

        return self._tournament_validation.validate_contact_numer(number)
    
    def validate_tournament_number_of_teams(self, num_of_teams: str) -> bool:
        '''Takes tournament number of teams of type string and checks if it is valid,
        Raises an error if number of teams is invalid'''

        return self._tournament_validation.validate_number_of_teams(num_of_teams)
    
    def validate_teams_in_tournament(self, team_to_tournament: str, teams_in_tournament: list) -> bool:
        '''Takes in name of team ment to be added to tournament and a list of teams already in tournament.
        Checks if team is already in tournament'''

        return self._tournament_validation.validate_teams_in_tournament(team_to_tournament, teams_in_tournament)
    
    def validate_tournament_id(self, id: str) -> bool:
        '''Takes tournament id of type string and checks if it is valid,
        Raises an error if id is invalid'''

        return self._tournament_validation.validate_id(id)
    
    def validate_servers(self, servers: str, num_of_teams: int) -> bool:
        '''Takes tournament server of type string and number of teams as int and checks if number of servers is valid,
        Raises an error if number of servers are invalid'''

        return self._tournament_validation.validate_servers(servers, num_of_teams)
    
    def does_tournament_id_exist(self, id: str) -> bool:
        '''Takes in tournament id of type str and cheks if a tournament with said in exists.
        Raises an error if tournament does not exist'''

        return self._tournament_validation.does_tournament_id_exist(id)

    


    


