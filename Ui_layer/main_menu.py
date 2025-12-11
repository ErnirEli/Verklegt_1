class MainMenu:
    def __init__(self):
        pass
    
    def __str__(self):
        return (
            "Choose your role\n"
            "---------------\n"
            "1.Spectator\n"
            "2.Captain\n"
            "3.Organiser\n"
            "\n"
            "9.Cancel\n"
            "---------------")
    
    def get_choice(self):
        """Ask user and return a validated choice."""
        while True:
            print(self)
            choice = input("Enter number: ").strip()

            if choice in {"1", "2", "3", "9"}:
                return choice
            
            print("Invalid choice. Try again.\n")

# choice = MainMenu()
# print(choice)