
from models.player import Player
from Datalayer.data_api import DataAPI


class PlayerLogic:


    def __init__(self, data_wrapper: DataAPI):
        self._data = data_wrapper

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
                    phone, email, link, handle, 
                    team_name, tournaments, wins, runner_up):
        '''Creates an instance of Player'''

        new_player = Player(handle, name, dob, address,
                            phone, email, link, team_name, 
                            tournaments, wins, runner_up)
        
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

        self._data.write_players(players)
        return

    def player_info(self, handle, role=None, private=False):
        
        players = self._data.get_all_players()
        player = self.find_player(players, handle)
        if player is None:
            return None

        if not private:
            return {
                "handle": player.handle,
                "team_name": player.team_name,
            }

        if not self.is_editor(role):
            return {"error": "Private data only for captains/organizers."}

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


