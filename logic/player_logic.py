
from models.player import Player
from Datalayer.data_api import DataAPI


class PlayerLogic:


    def __init__(self, data_wrapper: DataAPI):
        self._data = data_wrapper

    def is_editor(self, role):
        return role == "organizer" or role == "captain"

    def find_player(self, players, handle):
        for line in players:
            if line.handle == handle:
                return line
        return None


    def create_player(self, name, dob, address,
                      phone, email, link, handle, team_name, tournaments, wins):

        new_player = Player(handle, name, dob, address,
                            phone, email, link, team_name, tournaments, wins)
        self._data.add_player(new_player)
        

        return True

    def edit_player_info(self, handle,
                         new_phone=None, new_email=None,
                         new_address=None, new_link=None):


        players = self._data.get_all_players()
        player = self.find_player(players, handle)
        if player is None:
            return None

        if new_phone is not None:
            player.phone = new_phone
        if new_email is not None:
            player.email = new_email
        if new_address is not None:
            player.address = new_address
        if new_link is not None:
            player.link = new_link

        self._data.write_players(players)
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
        }

    def list_players_public(self):

        players = self._data.get_all_players()
        result = []
        for p in players:
            result.append({
                "handle": p.handle,
                "team_name": p.team_name
            })
        return result


