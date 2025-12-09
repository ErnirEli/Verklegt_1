from __future__ import annotations
from typing import Dict, Type, Optional

from lagaui import Captain, ChangeRole, CreateAClub, CreateAPlayer, CreateATournament, Organiser, SeeMatchResult, SeeMatchSchedule, SeeTournament, UIlayer, ViewTeams
#import validation að hvert og allt virkar from import validation...



class captain:
    "Captein getur búið til lið, mót og búið til leikmann"
    def __init__(self) -> None:
        # Valmynd: númer -> klasi sem á að keyrast
        self.options: Dict[str, Type[object]] = {
            "1": ViewTeams,
            "2": SeeTournament,
            "3": SeeMatchSchedule,
            "4": CreateAPlayer,
            "9": ChangeRole,
        }
        
        print("Captain class running!")

    def __str__(self) -> str:
        """Skilar streng sem sýnir valmynd fyrir fyrirliða."""
        return (
            "Captain\n"
            "---------------\n"
            "1. View Teams\n"
            "2. See Tournament\n"
            "3. See match schedule\n"
            "4. Create a player\n\n"
            "9. Change role\n"
            "---------------\n"
        "Enter number for action: "
    )

def run(self) -> Optional[object]:
    "Sýnir valmynd og skilar niðurstöðu að valda hlutverkinu"
    "Það skilar captain, spectator, orginaser, cancel og engu ef valið var ógilt"

    print(self)
    choice: str = input("Enter choice: ").strip()

    if choice in self.options:
        # Búum til instance af hlutverksklasanum.
        return self.options[choice]()  # type: ignore[call-arg]
    else:
        print("Invalid choice.")
        return None

