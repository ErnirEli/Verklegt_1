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

    # Lines

    S_LINE = '----------'
    M_LINE = '-------------------'
    L_LINE = '-----------------------------'

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
        bo: str = self.BOLD
        m: str = self.MAGENTA

        print(f"{bg}{" ":^19}{bo}{m}{" _                  _____                                                 _   ":<100}{re}")
        print(f"{bg}{"___":^19}{bo}{m}{"| |    __ _ _ __   |_   _|__  _   _ _ __ _ __   __ _ _ __ ___   ___ _ __ | |_ ":<100}{re}")
        print(f"{bg}{"|":>8}{r}{b}{"[_]"}{re}{bg}{"|":<8}{bo}{m}{"| |   / _` | '_ \    | |/ _ \| | | | '__| '_ \ / _` | '_ ` _ \ / _ \ '_ \| __|":<100}{re}")
        print(f"{bg}{"|+ ;|":^19}{bo}{m}{"| |__| (_| | | | |   | | (_) | |_| | |  | | | | (_| | | | | | |  __/ | | | |_":<100}{re}")
        print(f"{bg}{"`---'":^19}{bo}{m}{"|_____\__,_|_| |_|   |_|\___/ \__,_|_|  |_| |_|\__,_|_| |_| |_|\___|_| |_|\__|":<100}{re}")
        print(f"{bg}{" ":^119}{re}\n")


    def big_logo(self):
        bg: str = self.BLACK_BG
        c: str = self.CYAN
        r: str = self.RED        
        re: str = self.RESET

        print(f"{bg}{" "*100}")
        print(f"{c}{" "*15}{"████████╗██╗  ██╗██╗███████╗    ██╗███████╗    ██╗    ██╗██╗  ██╗██╗   ██╗":<85}")
        print(f"{c}{" "*15}{"╚══██╔══╝██║  ██║██║██╔════╝    ██║██╔════╝    ██║    ██║██║  ██║╚██╗ ██╔╝":<85}")
        print(f"{c}{" "*15}{"   ██║   ███████║██║███████╗    ██║███████╗    ██║ █╗ ██║███████║ ╚████╔╝ ":<85}")
        print(f"{c}{" "*15}{"   ██║   ██╔══██║██║╚════██║    ██║╚════██║    ██║███╗██║██╔══██║  ╚██╔╝  ":<85}")
        print(f"{c}{" "*15}{"   ██║   ██║  ██║██║███████║    ██║███████║    ╚███╔███╔╝██║  ██║   ██║   ":<85}") 
        print(f"{c}{" "*15}{"   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ":<85}")
        print(f"{c}{" "*20}{"██╗    ██╗███████╗     ██████╗██╗      █████╗ ███████╗██╗  ██╗":<80}")
        print(f"{c}{" "*20}{"██║    ██║██╔════╝    ██╔════╝██║     ██╔══██╗██╔════╝██║  ██║":<80}")
        print(f"{c}{" "*20}{"██║ █╗ ██║█████╗      ██║     ██║     ███████║███████╗███████║":<80}")
        print(f"{c}{" "*20}{"██║███╗██║██╔══╝      ██║     ██║     ██╔══██║╚════██║██╔══██║":<80}")
        print(f"{c}{" "*20}{"╚███╔███╔╝███████╗    ╚██████╗███████╗██║  ██║███████║██║  ██║":<80}")
        print(f"{c}{" "*20}{" ╚══╝╚══╝ ╚══════╝     ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝":<80}{re}\n")


    def top_bar(self):
        self.clear_screen()
        self.logo()

    def menu_top(self):
        self.clear_screen()
        self.big_logo()










