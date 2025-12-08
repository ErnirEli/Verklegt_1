from __future__ import annotations
from typing import Dict, Type, Optional

from chatverk import ChangeRole, CreateAClub, CreateAPlayer, CreateATournament, SeeMatchResult, SeeMatchSchedule, SeeTournament, ViewTeams
#import validation að hvert og allt virkar from import validation...

class Vew_Teams:
    "klasi sem maður getur séð liðin"

    def __init__(self) -> None:
        print("View teams selected")

class See_Tournument:
    "Klasi sem stendur fyrir að geta séð mótið"

    def __init__(self)-> None:
        print("See Tournument selected")

class See_Match_Schedule:
    "Klasi sem maður getur séð dagskrá á leikjum"

    def __init__(self)-> None:
        print("See Match Schedule selected")

class See_Match_Result:
    "klasi sem maður getur séð útkomu leikja"

    def __init__(self)-> None:
        print("See match result selected")

class Create_A_Player:
    "Klasi sem maður getur búið til leikmann"

    def __init__(self)-> None:
        print ("Create a player selected")

class Create_A_Tournoment:
    "Klasi sem hægt er að búa til mót"

    def __init__(self)-> None:
        print ("Create a tournoment selected")

class Create_A_Club:
    "Klasi sem hægt að búa til lið"

    def __init__(self)-> None:
        print ("Create a club selected")

class Change_Role:
    "Klasi sem táknar að notandi vilji skipta um hlutverk. Hlutverkaskipting er meðhöndluð í while lykkjunni"

    def __init__(self)-> None:
        print ("Change role selected")

class cancel:
    "Klasi sem táknar að notandi vill hætta í forritinu"

    def _init__(self)-> None:
        print ("cancel selected. Goodbye!")

    def run(self) -> None:
        """Skilar engu Þessi klasi er bara notaður til að brjóta út úr while-lykkjunni."""
        return None

class Orginaser:
    "Orginaser er skipuleggjari mótsins, sýnir valmynd og kallar á aðgerðir eftir vali notanda"
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

    def __str__(self)-> str:
        return (
            "þetta skilar inn streng sem sýnir valmynd"
            "Organiser\n\n"
            "1. View Teams\n"
            "2. See Tournament\n"
            "3. See match schedule\n"
            "4. Create a player\n"
            "5. Create a tournament\n"
            "6. Create a club\n\n"
            "9. Change role\n\n"
            "Enter a number for action:"
            )
    
    def run(self)-> Optional[Change_Role]:
        "keyrir valmyndina fyrir Organiser, change role ef notandi velur að skipta um hlutverk annars ekkert "

        print(self)
        choice: str = input("Enter choice: ").strip()
        if choice in self.options:
            
            action = self.options[choice]()  
        
            if isinstance(action, ChangeRole):
                return action
        else:
            print("Invalid choice.")

        return None

class Spectator:
    "(Áhorfandi) getur séð allt eins og t.d leikjadagskrá, úrslit, liðin, upplysíngar um lið, leikmenn, upplysíngar um leikmenn " 
     def __init__(self) -> None:
        # Valmynd: númer -> klasi sem á að keyrast
        self.options: Dict[str, Type[object]] = {
            "1": ViewTeams,
            "2": SeeTournament,
            "3": SeeMatchSchedule,
            "4": SeeMatchResult,
            "5": Players
            
            "9": ChangeRole,
        }









    
   
        

        


    






    
    




