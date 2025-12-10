from logic.logic_api import logicAPI


class SpectatorUI:

    def __init__(self):
        self._logic = logicAPI()

    def run(self):
        while True:
            print("\n=== Spectator Menu ===")
            print("1. List players")
            print("2. View player info")
            print("3. List tournaments (not implemented yet)")
            print("0. Back / exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                players = self._logic.list_players_public()
                print("\n--- Players ---")
                for p in players:
            # p is a dict: {'handle': '...', 'team_name': '...'}
                    print(f"Handle: {p['handle']}")
                    print(f"Team name: {p['team_name']}")
                    print("-" * 35)
            
            elif choice == "2":
                handle = input("Enter player handle: ").strip()
                player = self._logic.get_player_public_info(handle)
                if player is None:
                    print("No player found with that handle.")
                else:
        
                    print("\n--- Player info ---")
                    print(f"Handle: {player['handle']}")
                    print(f"Team name: {player['team_name']}")

            elif choice == "3":
                print("Listing tournaments not implemented yet.")

            elif choice == "0":
                print("Exiting spectator UI.")
                break

            else:
                print("Invalid option, try again.")

