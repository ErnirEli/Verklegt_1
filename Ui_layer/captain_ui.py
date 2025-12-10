from logic.logic_api import logicAPI
from organizer_ui import OrganizerUI

class Captain:

    def __init__(self) -> None:
        self._organizer = OrganizerUI()
        self._logic = logicAPI()

    def __str__(self) -> str:

        return (
            "Captain\n"
            "---------------\n"
            "1. View Teams\n"
            "2. See Tournament\n"
            "3. See match schedule\n"
            "4. Create a player\n"
            "\n"
            "9. Change role\n"
            "---------------\n"
        )

    def get_choice(self) -> str:
        """Biður notanda um val og skilar staðfestu vali (án dict)."""
        valid_choices = {"1", "2", "3", "4", "9"}  

        while True:
            print(self)
            choice = input("Enter number for action: ").strip()

            if choice in valid_choices:
                return choice

            print("Invalid choice. Try again.\n")

    def run(self):
        if self.get_choice == "1":
            teams = self._logic.list_teams()
            print(teams)

        elif self.get_choice == "2":
            tournament = self._logic.list_tournaments()
            print(tournament)
        
        elif self.get_choice == "3":
            match_schedule = self._logic.list_matches()
            print(match_schedule)
        
        elif self.get_choice == "4":
            self._organizer.create_player()

