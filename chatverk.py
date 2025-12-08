from __future__ import annotations
from typing import Dict, Type, Optional


class ViewTeams:
    """Aðgerð sem táknar að notandi vilji sjá lið."""

    def __init__(self) -> None:
        print("View teams class selected")


class SeeTournament:
    """Aðgerð sem táknar að notandi vilji sjá mót."""

    def __init__(self) -> None:
        print("See tournaments selected")


class SeeMatchSchedule:
    """Aðgerð sem táknar að notandi vilji sjá leikjadagskrá."""

    def __init__(self) -> None:
        print("Match schedule selected")


class SeeMatchResult:
    """Aðgerð sem táknar að notandi vilji sjá úrslit leikja."""

    def __init__(self) -> None:
        print("Seeing match result")


class CreateAPlayer:
    """Aðgerð sem táknar að leikmaður sé búinn til."""

    def __init__(self) -> None:
        print("Creating a player is selected")


class CreateATournament:
    """Aðgerð sem táknar að mót sé búið til."""

    def __init__(self) -> None:
        print("Create a tournament selected")


class CreateAClub:
    """Aðgerð sem táknar að félag sé búið til."""

    def __init__(self) -> None:
        print("Create club selected")


class ChangeRole:
    """
    Klasi sem táknar að notandi vilji skipta um hlutverk.
    Hlutverkaskipting er meðhöndluð í ytra while-lykkjunni.
    """

    def __init__(self) -> None:
        print("Changing role")


class Cancel:
    """
    Klasi sem táknar að notandi vilji hætta í forritinu.
    """

    def __init__(self) -> None:
        print("Cancel selected. Goodbye!")

    def run(self) -> None:
        """Skilar engu. Þessi klasi er bara notaður til að brjóta út úr while-lykkjunni."""
        return None


class Organiser:
    """
    Hlutverk: Skipuleggjandi mótsins (Organiser).
    Sýnir valmynd og kallar á viðeigandi aðgerðir eftir vali notanda.
    """

    def __init__(self) -> None:
        # Valmynd: númer -> klasi sem á að keyrast
        self.options: Dict[str, Type[object]] = {
            "1": ViewTeams,
            "2": SeeTournament,
            "3": SeeMatchSchedule,
            "4": CreateAPlayer,
            "5": CreateATournament,
            "6": CreateAClub,
            "9": ChangeRole,
        }

    def __str__(self) -> str:
        """Skilar streng sem sýnir valmynd fyrir skipuleggjanda."""
        return (
            "Organiser\n\n"
            "1. View Teams\n"
            "2. See Tournament\n"
            "3. See match schedule\n"
            "4. Create a player\n"
            "5. Create a tournament\n"
            "6. Create a club\n\n"
            "9. Change role\n\n"
            "Enter a number for action: "
        )

    def run(self) -> Optional[ChangeRole]:
        """
        Keyrir valmyndina fyrir skipuleggjanda.

        Returns:
            ChangeRole ef notandi velur að skipta um hlutverk,
            annars None.
        """
        print(self)
        choice: str = input("Enter choice: ").strip()

        if choice in self.options:
            # Búum til instance af þeim klasa sem var valinn.
            action = self.options[choice]()  # type: ignore[call-arg]
            # Ef notandinn valdi að skipta um hlutverk, sendum það til baka.
            if isinstance(action, ChangeRole):
                return action
        else:
            print("Invalid choice.")

        return None


class Spectator:
    """
    Hlutverk: Áhorfandi (Spectator).
    Getur séð lið, mót, leikjadagskrá og úrslit.
    """

    def __init__(self) -> None:
        # Valmynd: númer -> klasi sem á að keyrast
        self.options: Dict[str, Type[object]] = {
            "1": ViewTeams,
            "2": SeeTournament,
            "3": SeeMatchSchedule,
            "4": SeeMatchResult,
            "9": ChangeRole,
        }

    def __str__(self) -> str:
        """Skilar streng sem sýnir valmynd fyrir áhorfanda."""
        return (
            "Spectator\n"
            "-------------\n"
            "1. View Teams\n"
            "2. See Tournaments\n"
            "3. See match schedule\n"
            "4. See results\n\n"
            "9. Change role\n"
            "---------------\n"
            "Enter number for action: "
        )

    def run(self) -> Optional[ChangeRole]:
        """
        Keyrir valmyndina fyrir áhorfanda.

        Returns:
            ChangeRole ef notandi velur að skipta um hlutverk,
            annars None.
        """
        print(self)
        choice: str = input("Enter choice: ").strip()

        if choice in self.options:
            action = self.options[choice]()  # type: ignore[call-arg]
            if isinstance(action, ChangeRole):
                return action
        else:
            print("Invalid choice.")

        return None


class Captain:
    """
    Hlutverk: Fyrirliði liðs (Captain).
    Getur séð lið, mót, leikjadagskrá og búið til leikmann.
    """

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

    def run(self) -> Optional[ChangeRole]:
        """
        Keyrir valmyndina fyrir fyrirliða.

        Returns:
            ChangeRole ef notandi velur að skipta um hlutverk,
            annars None.
        """
        print(self)
        choice: str = input("Enter choice: ").strip()

        if choice in self.options:
            action = self.options[choice]()  # type: ignore[call-arg]
            if isinstance(action, ChangeRole):
                return action
        else:
            print("Invalid choice.")

        return None


class UIlayer:
    """
    Efsta UI lagið.
    Sér um að velja hlutverk (Spectator, Captain, Organiser) eða hætta (Cancel).
    """

    def __init__(self) -> None:
        # Valmynd: númer -> hlutverksklasi
        self.options: Dict[str, Type[object]] = {
            "1": Spectator,
            "2": Captain,
            "3": Organiser,
            "9": Cancel,
        }

    def __str__(self) -> str:
        """Skilar streng sem sýnir hlutverksvalmynd."""
        return (
            "Choose your role\n"
            "---------------\n"
            "1. Spectator\n"
            "2. Captain\n"
            "3. Organiser\n"
            "\n"
            "9. Cancel\n"
            "---------------"
        )

    def run(self) -> Optional[object]:
        """
        Sýnir hlutverksvalmynd og skilar instance af valda hlutverkinu.

        Returns:
            Spectator, Captain, Organiser eða Cancel instance,
            eða None ef val var ógilt.
        """
        print(self)
        choice: str = input("Enter choice: ").strip()

        if choice in self.options:
            # Búum til instance af hlutverksklasanum.
            return self.options[choice]()  # type: ignore[call-arg]
        else:
            print("Invalid choice.")
            return None


# ---- Aðal keyrsla forrits ----

ui = UIlayer()

while True:
    # Fyrst er valið hlutverk (role)
    role = ui.run()

    if role is None:
        # Ógilt val, byrja upp á nýtt
        continue

    if isinstance(role, Cancel):
        # Notandi valdi að hætta
        break

    # Ef hlutverk er Spectator, Organiser eða Captain
    if isinstance(role, (Spectator, Organiser, Captain)):
        while True:
            # Keyrir valmyndina fyrir viðkomandi hlutverk
            result = role.run()

            # Ef notandi velur að skipta um hlutverk
            if isinstance(result, ChangeRole):
                role = None
                break

print("Program ended.")
