class Organiser:
    def __init__(self):
        self.options = { 
            "1" : ViewTeams,
            "2" : SeeTournament,
            "3" : SeeMatchSchedule,
            "4" : CreateAPlayer,
            "5" : CreateATournament,
            "6" : CreateAClub,
            "9" : ChangeRole
         }
        

    def __str__(self):
        return (
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
    
    
    
    def run(self):
        print(self)
        choice = input("Enter choice: ").strip()

        if choice in self.options:
            action = self.options[choice]()
            if isinstance(action, ChangeRole):
                return action
                  
        else:
            print("Invalid choice.")
            return None
    
   
    

        print("Organiser class running!")
class CreateAPlayer:
    def __init__(self):
        print("Creating a player is selected")
        
class CreateATournament:
    def __init__(self):
        print("Create a Tournament selected")
        
class CreateAClub:
    def __init__(self):
        print("Create club selected")
        
class Spectator:
    
    
    def __init__(self):
        self.options = {
            "1" : ViewTeams,
            "2" : SeeTournament,
            "3" : SeeMatchSchedule,
            "4" : SeeMatchResult,
            "9" : ChangeRole
        }
    def __str__(self):
        return (
            "Spectator\n"
            "-------------\n"
            "1. View Teams\n"
            "2. See Tournaments\n"
            "3. See match schedule\n"
            "4. See results\n\n"
            "9. Change role\n"
            "---------------\n"
            "Enter number for action"
        )
    def run(self):
        print(self)
        choice = input("Enter choice: ").strip()

        if choice in self.options:
            action = self.options[choice]()
            if isinstance(action, ChangeRole):
                return action
                  
        else:
            print("Invalid choice.")
            return None
    
    

    
    
       ##print("Spectator class running!")

class Captain:
    def __init__(self):
       
        self.options = {
            "1": ViewTeams,
            "2": SeeTournament,
            "3": SeeMatchSchedule,
            "4": CreateAPlayer,
            "9": ChangeRole,
        }
        print("Captain class running!")


    def __str__(self):
        return (
        "Captain\n"
        "---------------\n"
        "1. View Teams\n"
        "2. See Tournament\n"
        "3. See match schedule\n"
        "4. Create a player\n\n"
        "9. Change role\n"
        "---------------\n"
        "Enrer number for action:"
        )



    def run(self):
        print(self)
        choice = input("Enter choice: ").strip()

        if choice in self.options:
            action = self.options[choice]()
            if isinstance(action, ChangeRole):
                return action
                  
        else:
            print("Invalid choice.")
            return None
    
        

class Cancel:
    def __init__(self):
        print("Cancel selected. Goodbye!")
    def run(self):
        return None   
class ViewTeams:
    def __init__(self):
        print("View teams class selected")
        

    
        

class SeeTournament:
    def __init__(self):
        print("see tournaments selected")
 
class SeeMatchSchedule:
    def __init__(self):
        print("match Schedule")
         
class SeeMatchResult:
    def __init__(self):
        print("Seeing Match Result")
        
class ChangeRole:
    def __init__(self):
        print("Changing role")
       
        



class UIlayer:
    def __init__(self):
        # Choice --> Class
        self.options = {
            "1": Spectator,
            "2": Captain,
            "3": Organiser,
            "9": Cancel
        }

    def __str__(self):
        return (
            "Choose your role\n"
            "---------------\n"
            "1.Spectator\n"
            "2.Captain\n"
            "3.Organiser\n"
            "\n"
            "9.Cancel\n"
            "---------------"
        )

    def run(self):
        print(self)
        choice = input("Enter choice: ").strip()

        if choice in self.options:
            return self.options[choice]()  # Instantiate selected class
        else:
            print("Invalid choice.")
            return None
   
ui = UIlayer()
while True:
    role = ui.run()
    if role is None:
        continue
    if isinstance(role, Cancel):
        break  

   
    if isinstance(role, (Spectator, Organiser, Captain)):
       while True:
            result = role.run()
            if isinstance(result, ChangeRole):
                role = None
                break

        

print("Program ended.")














Spect = Spectator()
"""
Org = Organiser()
Org.run()"""


