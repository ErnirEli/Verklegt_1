from __future__ import annotations
from typing import Dict, Type, Optional

from lagaui import Captain, ChangeRole, CreateAClub, CreateAPlayer, CreateATournament, Organiser, SeeMatchResult, SeeMatchSchedule, SeeTournament, UIlayer, ViewTeams
#import validation að hvert og allt virkar from import validation... 

class Spectator:
    "(Áhorfandi) getur séð allt eins og t.d leikjadagskrá, úrslit, liðin, upplysíngar um lið, leikmenn, upplysíngar um leikmenn " 
     
     
    def __init__(self) -> None:
        # Valmynd: númer -> klasi sem á að keyrast
        self.options: Dict[str, Type[object]] = {
            "1": ViewTeams,
            "2": SeeTournament,
            "3": SeeMatchSchedule,
            "4": SeeMatchResult,
            "5": players, # bætti þessu við
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
    