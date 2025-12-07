
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

        """Using player model to get the right format before adding the created player
        to Database"""
        new_player = Player(handle, name, dob, address,
                            phone, email, link, team_name, tournaments, wins)
        self._data.add_player(new_player)
        

        return "Player created."

    def edit_player_info(self, handle,
                         new_phone=None, new_email=None,
                         new_address=None, new_link=None):


        players = self._data.get_all_players()          # Gets data from the data layer
        player = self.find_player(players, handle)      # Use the definition above to find the player by 
        if player is None:                              # Scouring each line until it finds a match 
            return "Player not found."

        """Override checks here: where if a change is
        made then its saved and overrides its original data"""

        if new_phone is not None:
            player.phone = new_phone
        if new_email is not None:
            player.email = new_email
        if new_address is not None:
            player.address = new_address
        if new_link is not None:
            player.link = new_link

        self._data.rewrite_players(players)             # Changes saved to database
        return True, "Player info updated."

    def player_info(self, handle, role=None, private=False):
        
        players = self._data.get_all_players()          # Pulling player data
        player = self.find_player(players, handle)      # Finding if the searched player available
        if player is None:
            return None

        if not private:                                 # Privacy is determined by role
            return {                                    # Returns only player and handle if privacy is still false
                "handle": player.handle,
                "team_name": player.team_name,
            }

        if not self.is_editor(role):
            return {"error": "Private data only for captains/organizers."}

        """ Returns all Player data if all requirements are met"""

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
        return result           # Returns all info on all players handle and their name


