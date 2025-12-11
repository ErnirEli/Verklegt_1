from Datalayer.data_api import DataAPI
from Error.team_error import *
from models.player import Player
from Error.general_error import EmptyInput


class ValidateTeam:
    def __init__(self):
        self._data = DataAPI()
    
    def validate_name(self, name: str):
        if not name:
            raise EmptyInput
        
        team_list = self._data.get_all_teams()

        for team in team_list:
            if name.strip() == team.name:
                raise TeamExistsError
        
        return True

    def validate_captain(self, captain: str, players_in_team: list):
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

    def validate_web_link(self, web_link: str):
        if web_link == "https://":
            raise EmptyInput
        if "." not in web_link:
            raise InvalidWebLink
        return True

    def validate_ascii_logo(self, ascii):
        if not ascii:
            raise EmptyInput
        return True
    
    def validate_number_of_players(self, num_of_players: str):
        num_of_players = int(num_of_players)
        
        if not num_of_players:
            raise EmptyInput
        if num_of_players > 5:
            raise TooManyPlayersError
        if num_of_players < 3:
            raise NotEnoughPlayersError
        
        return True
    
    def validate_players_in_team(self, player_to_team: Player, players_in_team):
        all_players = self._data.get_all_players()
        all_player_handles = []

        for player in all_players:
            all_player_handles.append(player.handle)
        
        if player_to_team not in all_player_handles:
            raise PlayerDoesNotExistError
    
        
        if player_to_team in players_in_team:
            raise PlayerAlreadyInTeamError
        
        if player_to_team.team_name != "":
            raise playerNotAvailableError
        
        
        
        
        return True
        