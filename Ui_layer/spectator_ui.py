from logic.logic_api import logicAPI
from organizer_ui import OrganizerUI
 

class Spectator:
    "(Áhorfandi) getur séð allt eins og t.d leikjadagskrá, úrslit, liðin, upplysíngar um lið, leikmenn, upplysíngar um leikmenn " 
    def __init__(self):
        self._logic = logicAPI()
        self._organizer = OrganizerUI

    def __str__(self):
        return (
            "Spectator\n"
            "-------------\n"
            "1. View Teams\n"
            "2. See Tournaments\n"
            "3. See match schedule\n"
            "4. See results\n"
            "5. View players\n\n"
            "9. Change role\n"
            "---------------\n"
        )
     
    
    def get_choice(self):
        """Ask user and return a validated choice."""
        while True:
            print(self)
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "5", "6" "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")

    def run(self):
   
        choice = self.get_choice()

        if choice == "1":
            ViewTeams()
        elif choice == "2":
            SeeTournament()
        elif choice == "3":
            SeeMatchSchedule() 
        elif choice == "4":
            SeeMatchResult()
        elif choice == "5":
            players()      # klasinn sem ég bætti við
        elif choice == "9":
            return ChangeRole()   # skilar hlutverki svo main geti skipað um hlutverk

        return None 
