from typing import List
from logic.team_logic import TeamLogic
from models.team import Team
from Datalayer.data_api import DataAPI
#from logic.tournament_logic import TournamentLogic
from logic.match_logic import MatchLogic
#from models.tournament  import Tournament
from models.match import Match
from logic.club_logic import ClubLogic
from models.club import Club
from logic.player_logic import PlayerLogic
from models.player import Player


class logicAPI:

    def __init__(self) -> None:
        data_api: DataAPI = DataAPI()
        self._team_logic = TeamLogic()
        #self._tournament_logic = TournamentLogic(data_api)
        self._match_logic = MatchLogic(data_api)
        self._club_logic = ClubLogic(data_api)
        self._player_logic = PlayerLogic()
#Teams
    def list_teams(self) -> list[Team]:
        return self._team_logic.list_all_teams()
    
    def create_team(self,name: str, captain: str, web_link: str, ASCII = str) -> Team:
        return self._team_logic.create_team(name, captain, web_link, ASCII )

#Tournaments

    #def list_tournaments(self) -> None:
        #return self._tournament_logic.list_all_tournaments()
    
    #def create_tournament(self, start_date: int, end_date: int, name: str, venue: str, contract: str, contact_person: tuple, team_list: list) -> List[Tournament]:
        #return self._tournament_logic.create_tournaments(start_date, end_date, name, venue, contract, contact_person, team_list)
#Matches
    
    def list_matches(self) -> None:
        return self._match_logic.list_all_matches()
    # def create_match(self,teams: tuple):
    #     return self._match_logic.create_match(teams)
    
#Clubs

    def list_clubs(self) -> None:
        return self._club_logic.list_all_clubs()
    
    def create_club(self, name: str, colors: str, hometown: str, country: str) -> List:
        return self._club_logic.create_club(name, colors, hometown, country)

#Player
    def create_player(self, name: str, dob: str, address: str, phone: str, email: str,
                      link: str, handle: str, team_name: str, tournaments: int, wins: int) -> Player:
        """Creates a new player and adds them to the database"""
        return self._player_logic.create_player( name, dob, address, phone, email, link, handle, team_name, tournaments, wins)
    
    def edit_player_info(self, handle: str, new_phone = None,  new_email = None, new_address = None, new_link = None) -> bool:
        """Edits player info returns True if the changes have been made"""
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