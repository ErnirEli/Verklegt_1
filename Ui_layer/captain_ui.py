from typing import Optional
from lagaui import ChangeRole, CreateAPlayer, SeeMatchSchedule, SeeTournament, ViewTeams
from validation.player_validation import ValidatePlayer
from logic.player_logic import PlayerLogic


class Captain:
    """Captain getur búið til lið, mót og búið til leikmann."""

    def __init__(self) -> None:
       
        self.validate_player = ValidatePlayer()
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

    def run(self) -> Optional[ChangeRole]:
        """
        Keyrir valmyndina fyrir Captain.
        Skilar ChangeRole ef notandi velur að skipta um hlutverk, annars None.
        """
        choice = self.get_choice()

        if choice == "1":
            ViewTeams()
        elif choice == "2":
            SeeTournament()
        elif choice == "3":
            SeeMatchSchedule()
        elif choice == "4":
            CreateAPlayer()

        elif choice == "9":
            return ChangeRole()

        return None

