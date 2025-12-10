from logic.logic_api import logicAPI

class Captain:
    """Captain getur búið til lið, mót og búið til leikmann."""

    def __init__(self) -> None:
       
        self._logic = logicAPI()
        print("Captain class running!")

    def __str__(self) -> str:
        """Skilar streng sem sýnir valmynd fyrir fyrirliða."""
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
        if self.get_choice == 1:
            teams = self._logic.list_teams()
            print(teams)

