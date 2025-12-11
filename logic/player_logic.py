
from models.player import Player
from Datalayer.data_api import DataAPI


class PlayerLogic:


    def __init__(self):
        self._data = DataAPI()

    def is_editor(self, role):
        return role == "organizer" or role == "captain"

    def find_player(self, players, handle):
        '''Finds a single player based on handle'''

        for player in players:
            player: Player

            if player.handle == handle:
                return player
        return None


    def create_player(self, name, dob, address,
                    phone, email, link, handle):

        new_player = Player(name, dob, address,
                            phone, email, link, handle)
        self._data.add_player(new_player)
        
        return 

    def edit_player_info(self, handle,
                        new_phone = False, new_email = False,
                        new_address = False, new_link = False):
        '''Edits desired player info'''


        players = self._data.get_all_players()
        player = self.find_player(players, handle)
        
        # if player is None:
        #     return

        if new_phone:
            player.phone = new_phone
        if new_email:
            player.email = new_email
        if new_address:
            player.address = new_address
        if new_link:
            player.link = new_link

        self._data.rewrite_players(players)
        return True

    def get_public_player_info(self, handle: str):
        players = self._data.get_all_players()
        player = self.find_player(players, handle)
        if player is None:
            return None

        return {
            "handle": player.handle,
            "team_name": player.team_name,
        }
            

    def get_full_player_info(self, handle: str):
        players = self._data.get_all_players()
        player = self.find_player(players, handle)
        if player is None:
            return None

        return {
            "name": player.name,
            "dob": player.dob,
            "address": player.address,
            "phone": player.phone,
            "email": player.email,
            "link": player.link,
            "handle": player.handle,
            "team_name": player.team_name,
            "tournaments": player.tournament,
            "wins": player.wins
        }

    def list_players_public(self):

        players = self._data.get_all_players()
        result = []
        for p in players:
            result.append({
                "handle": p.handle,
                "team_name": p.team_name,
                "tournaments": p.tournaments
            })
        return result


