from Datalayer.data_api import DataAPI
from Error.team_error import *


class ValidateTeam:
    def __init__(self):
        self._data = DataAPI()
    
    def is_captain_or_organizer(self):
        #Á eftir að implementa
        return

    def validate_name(self, name: str):
        if not name:
            raise Emptyinput
        
        team_list = self._data.get_all_teams()

        for team in team_list:
            if name.strip() == team.name:
                raise TeamExistsError
        
        return True

    def validate_captain(self, captain: str):
        if not captain:
            raise Emptyinput
        
        all_players = self._data.get_all_players()
        player_names = []

        for player in all_players:
            player_names.append(player.handle)
        if captain not in player_names:
            raise CaptainNotExistError
        
    
        return True

    def validate_web_link(self, web_link: str):
        if web_link == "https://":
            raise Emptyinput
        if "." not in web_link:
            raise InvalidWebLink
        return True

    def validate_ascii_logo(self, ascii):
        if not ascii:
            raise Emptyinput
        return True
        