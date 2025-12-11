from Ui_layer.ui_constants import UIHelper

class MainMenu:

    def __init__(self):
        self.ui = UIHelper()

    def show_main_menu(self):
        choice = "q"
        while choice not in ("1", "2", "3", "9"):
            self.ui.top_bar()
            print (
                "Choose a role:\n\n"
                "1. Spectator\n"
                "2. Captain\n"
                "3. Organizer\n\n"
                "9. Quit"
                
                )
            choice = input()
            
        return choice
        
        
        

        
    


    
    
    def __str__(self):
        return