# from Datalayer.data_api import DataAPI
# from logic.team_logic import TeamLogic
# from models.team import Team
# from models.player import Player
from Ui_layer.organizer_ui import *

yo = OrganizerUI()

choice = yo.get_choice()
if choice == "7":
    yo.edit_player_info()
