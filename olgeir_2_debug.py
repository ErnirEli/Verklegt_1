from Datalayer.data_api import DataAPI
from logic.team_logic import TeamLogic
from models.team import Team
from models.player import Player
import csv

def main():
    # Initialize data layer
    data_api = DataAPI()
    logic = TeamLogic(data_api)

    logic.create_team(
        "Olgeir fc",
        "Olgeir", 
        "goat.com",
        """
 ____ |  |    ____   ____ |__|______      _/ ____\____  
 /  _ \|  |   / ___\_/ __ \|  \_  __ \     \   __\/ ___\ 
(  <_> )  |__/ /_/  >  ___/|  ||  | \/      |  | \  \___ 
 \____/|____/\___  / \___  >__||__|         |__|  \___  >
            /_____/      \/                           \/"""
        )
            
                    
           

main()