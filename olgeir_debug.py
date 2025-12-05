from Datalayer.data_api import DataAPI
from logic.team_logic import TeamLogic
from models.team import Team
from models.player import Player

def main():

    # Initialize data layer
    data_api = DataAPI()

    # Initialize the logic layer
    logic = TeamLogic(data_api)

    print("\n--- Loading teams from CSV ---")
    teams = logic.list_all_teams()

    if not teams:
        print("No teams found in CSV.\n")
    else:
        print(f"{len(teams)} teams loaded:")
        for t in teams:
            print(f"- {t.name}")
    print("--------------------------------\n")

    # --- Show full team details ---
    print("--- Team info from CSV ---")
    for team in teams:
        print(logic.team_info(team))
        print("--------------------------")

    # --- Show all players from CSV ---
    print("\n--- Loading players from CSV ---")
    players = data_api.get_all_players()

    if not players:
        print("No players found in CSV.\n")
    else:
        print(f"{len(players)} players loaded:")
        for p in players:
            print(f"- {p.name}, age {p.dob}")

    print("\nDone!")

if __name__ == "__main__":
    main()