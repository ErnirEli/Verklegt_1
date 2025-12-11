from typing import List
from logic.team_logic import TeamLogic
from models.team import Team
from logic.tournament_logic import TournamentLogic
from logic.match_logic import MatchLogic
from models.tournament  import Tournament
from models.match import Match
from logic.club_logic import ClubLogic
from models.club import Club
from logic.player_logic import PlayerLogic
from models.player import Player


class logicAPI:

    def __init__(self) -> None:
        self._team_logic = TeamLogic()
        self._tournament_logic = TournamentLogic()
        self._match_logic = MatchLogic()
        self._club_logic = ClubLogic()
        self._player_logic = PlayerLogic()

#Teams

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

        self._team_logic.get_team(team_name)

        return
    

#Tournaments

    def list_tournaments(self) -> list[Tournament]:
        '''Takes in nothing and returns a list of all existing tournaments of type Tournament'''

        return self._tournament_logic.list_all_tournaments()
    
    def get_tournament(self, tournament_id: str) -> Tournament:
        '''Takes in tournament ID and returns the torunament of type Torunament.
        Only runs after all validation checks are valid.'''

        self._tournament_logic.get_tournament(tournament_id)

    def create_tournament(self, tournament_id: str, name: str, venue: str,
                        start_date: str, end_date: str, contact: str, contact_email: str,
                        contact_number: str, servers: int, team_list: list[str]) -> Tournament:
        '''Takes in id, name, venue, start & end dates, contact, mail & number, servers, for a tournament, all of type string.
        also takes in a list of team names of type string. Creates a tournament using this info and adds all teams from the list to the torunament.
        Only runs after all validation checks are valid.'''

        return self._tournament_logic.create_tournament(tournament_id, name, venue, end_date, start_date,
                                                        contact, contact_email, contact_number, servers, team_list)


#Matches
    
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


#Clubs

    def list_clubs(self) -> None:
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


#Player

    def create_player(self, name: str, dob: str, address: str, phone: str, email: str,
                    link: str, handle: str, team_name: str) -> None:
        '''Takes in name, date of birth, adress, phone number, email, link, and hadle.
        Creates a player of type "Club" and saves him in the player CSV file.
        Only runs after all Validation checks are valid'''

        self._player_logic.create_player(name, dob, address, phone, email, link, handle, team_name)
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
    
    def get_player_public_info(self, handle: str):
        """Displays public player info 'Handle' and 'Name'"""
        return self._player_logic.get_public_player_info(handle)
    
    def get_player_full_info(self, handle: str):
        """Displays info on players that captains and organizers can see"""
        return self._player_logic.get_full_player_info(handle)
    
    def list_players_public(self):
        """Returns list of all players"""
        return self._player_logic.list_players_public()
    
    def get_player_private_info(self, handle: str):
        """Displays private player"""
        return self._player_logic.get_full_player_info(handle)