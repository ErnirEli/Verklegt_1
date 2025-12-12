from Datalayer.data_api import DataAPI
from Error.team_error import *
from models.player import Player
from Error.general_error import EmptyInput, BackButton


class ValidateTeam:
    def __init__(self):
        self._data = DataAPI()
    
    def validate_name(self, name: str) -> bool:
        '''Takes team name of type string and checks if it is valid,
        Raises an error if name of teams is invalid'''

        if name.lower() == "q":
            raise BackButton
        
        if not name:
            raise EmptyInput
        
        team_list = self._data.get_all_teams()

        for team in team_list:
            if name.strip() == team.name:
                raise TeamExistsError
        
        return True

    def validate_captain(self, captain: str, players_in_team: list) -> bool:
        '''Takes team captain handle of type string and a list of players in team, checks if captain is valid,
        Raises an error if captain is invalid'''

        if captain.lower() == "q":
            raise BackButton
        
        if not captain:
            raise EmptyInput
        
        all_players = self._data.get_all_players()
        player_handles = []

        for player in all_players:
            player_handles.append(player.handle)
        if captain not in player_handles:
            raise CaptainNotExistError
        if captain not in players_in_team:
            raise CaptainNotInTeamError
        
    
        return True

    def validate_web_link(self, web_link: str) -> bool:
        '''Takes team link of type string and checks if it is valid,
        Raises an error if link is invalid'''

        if web_link.lower() == "q":
            raise BackButton
        
        if web_link == "https://":
            raise EmptyInput
        if "." not in web_link:
            raise InvalidWebLink
        return True

    def validate_ascii_logo(self, ascii: str) -> bool:
        '''Takes team logo of type string and checks if it is valid,
        Raises an error if logo is invalid'''

        if not ascii:
            raise EmptyInput
        
        return True
    
    def validate_number_of_players(self, num_of_players: str) -> bool:
        '''Takes number of players in team of type string and checks if it is valid,
        Raises an error if number of players is invalid'''

        if num_of_players.lower() == "Q":
            raise BackButton
        
        num_of_players: int = int(num_of_players)
        
        if not num_of_players:
            raise EmptyInput
        if num_of_players > 5:
            raise TooManyPlayersError
        if num_of_players < 3:
            raise NotEnoughPlayersError
        
        return True
    
    def validate_players_in_team(self, player_to_team: str, players_in_team: list[str]) -> bool:
        '''Takes in a player name of type string and a list of players already in the team, of type string.
        checks if player is already in team.
        raises error of player is already in team.'''
        
        if player_to_team.lower() == "q":
            raise BackButton
        
        all_players = self._data.get_all_players()

        for player in all_players:
            player: Player

            if player.handle == player_to_team:
                break
        
        else:
            raise PlayerDoesNotExistError
    

        if player_to_team in players_in_team:
            raise PlayerAlreadyInTeamError
        
        if player.team_name != "None":
            raise playerNotAvailableError
        
        
        
        
        return True
        