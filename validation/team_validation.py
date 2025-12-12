from Datalayer.data_api import DataAPI
from Error.team_error import *
from models.player import Player
from Error.general_error import EmptyInput, BackButton
from models.team import Team


class ValidateTeam:
    def __init__(self):
        self._data = DataAPI()
    
    def validate_name(self, name: str):
        if name.lower() == "q":
            raise BackButton
        
        if not name:
            raise EmptyInput
        
        team_list = self._data.get_all_teams()

        for team in team_list:
            if name.strip() == team.name:
                raise TeamExistsError
        
        return True

    def validate_captain(self, captain: str, players_in_team: list):
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

    def validate_web_link(self, web_link: str):
        if web_link.lower() == "q":
            raise BackButton
        
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
        if num_of_players.lower() == "Q":
            raise BackButton
        
        num_of_players = int(num_of_players)
        
        if not num_of_players:
            raise EmptyInput
        if num_of_players > 5:
            raise TooManyPlayersError
        if num_of_players < 3:
            raise NotEnoughPlayersError
        
        return True
    
    def validate_players_in_team(self, player_to_team: str, players_in_team: list = []):
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
        
    def validate_player_to_remove(self, player_name: str):
        
        all_players = self._data.get_all_players()

        for player in all_players:
            player: Player

            if player.handle == player_name:
                break
        
        else:
            raise PlayerDoesNotExistError

        return True
        
        
        
        