from logic.logic_api import logicAPI


class SpectatorUI:

    def __init__(self, logic: logicAPI):
        self._logic = logic

    def run(self):
        while True:
            print("\n=== Spectator Menu ===")
            print("1. List players")
            print("2. View player info")
            print("3. List tournaments")
            print("0. Back / exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.list_players()
            elif choice == "2":
                self.view_player()
            elif choice == "3":
                self.list_tournaments()
            elif choice == "0":
                break
            else:
                print("Invalid choice, try again.")
