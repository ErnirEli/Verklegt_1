import os


class UIHelper():
    RESET = '\033[0m'
    # Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE =  '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # BG Colors
    BLACK_BG = '\033[40m'

    # Styles
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    BLINKING = '\033[5m'

    def clear_screen(self):
        '''Takes in nothing and clears screen from previous things'''

        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def logo(self):
        '''Takse in nothing and prints a logo in a formatted way'''

        bg: str = self.BLACK_BG
        r: str = self.RED
        b: str = self.BLINKING
        re: str = self.RESET

        print(f"{bg}{"___":^15}{re}")
        print(f"{bg}{"|":>6}{r}{b}{"[_]"}{re}{bg}{"|":<6}{re}")
        print(f"{bg}{"|+ ;|":^15}{re}")
        print(f"{bg}{"`---'":^15}{re}")
        print(f"{bg}{"":^15}{re}")

    def top_bar(self):
        self.clear_screen()
        self.logo()
