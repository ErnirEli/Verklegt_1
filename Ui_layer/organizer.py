class OrganizerMenu:
        def __init__(self):
              pass    
        
        
        
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
            )

        def get_choice(self):
            """Ask user and return a validated choice."""
            while True:
                print(self)
                choice = input("Enter number for action: ").strip()

                if choice in {"1", "2", "3", "4", "5", "6" "9"}:
                    return choice
            
                print("Invalid choice. Try again.\n")