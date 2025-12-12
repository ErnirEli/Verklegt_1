from Ui_layer.ui_constants import UIHelper

class MainMenu:

    def __init__(self):
        self._ui = UIHelper()

    def show_main_menu(self):
        '''Ui of main menu, takes in nothing and returns a choice of type str'''
        choice = ""
        while choice not in ("1", "2", "3", "q"):
            self._ui.menu_top()
            print (
                "Choose a role:\n\n"
                "1. Spectator\n"
                "2. Captain\n"
                "3. Organizer\n\n"
                "q. Quit\n\n"
                
                )
            choice = input("Choose role:\n")
            
        return choice
