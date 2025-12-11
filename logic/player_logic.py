
from models.player import Player
from Datalayer.data_api import DataAPI


class PlayerLogic:


    def __init__(self):
        self._data_api = DataAPI()

    def is_editor(self, role):
        return role == "organizer" or role == "captain"

    def find_player(self, handle: str) -> Player:
        '''Takes in a player handle of type string.
        Returns the player with same handle of type "Player".
        Only runs after all Validation checks are valid.'''

        players: list[Player] = self._data_api.get_all_players()

        for player in players:

            if player.handle == handle:
                return player

    def create_player(self, name: str, dob: str, address: str,
                    phone: str, email: str, link: str, handle: str) -> None:
        '''Takes in name, date of birth, adress, phone number, email, link, and hadle.
        Creates a player of type "Club" and saves him in the player CSV file.
        Only runs after all Validation checks are valid'''

        new_player = Player(name, dob, address, phone, email, link, handle)
        self._data_api.add_player(new_player)
        
        return True

    def edit_player_info(self, handle,
                        new_phone = False, new_email = False,
                        new_address = False, new_link = False) -> Player:
        '''Takes in a player handle and 1-4 of the following arguments: 
        phone number, email, address, link and changes the info for the player.
        Only runs if all Validation checks are valid.'''

        players: list[Player] = self._data_api.get_all_players()

        # Find the correct player
        for player in players:
            if player.handle == handle:
                break

        # Change desired things
        if new_phone:
            player.phone = new_phone
        if new_email:
            player.email = new_email
        if new_address:
            player.address = new_address
        if new_link:
            player.link = new_link

        self._data_api.write_players(players)
        return player

    def get_public_player_info(self, handle: str):
        players = self._data_api.get_all_players()
        player = self.find_player(players, handle)
        if player is None:
            return None

        return {
            "handle": player.handle,
            "team_name": player.team_name,
        }
            

    def get_full_player_info(self, handle: str):
        players = self._data_api.get_all_players()
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
            "tournament": player.tournament,
            "wins": player.wins
        }

    def list_players_public(self):

        players = self._data_api.get_all_players()
        result = []
        for p in players:
            result.append({
                "handle": p.handle,
                "team_name": p.team_name,
                "tournaments": p.tournaments
            })
        return result


