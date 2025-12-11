# from Datalayer.data_api import DataAPI
# from logic.team_logic import TeamLogic
# from models.team import Team
# from models.player import Player
from Ui_layer.organizer_ui import *

yo = OrganizerUI()

choice = yo.get_choice()
if choice == "4":
    yo.create_player()


if choice == "5":
    yo.create_tournoment()


if choice == "7":
    yo.create_team()

if choice == "6":
    yo.create_club()