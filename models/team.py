


class Team:
    name: str
    captain: str
    web_link: str
    ASCII: str
    tour_ID: str
    torunament: int
    wins: int
    runner_up: int

    def __init__(self, name: str, captain: str, club: str = 'None',
                web_link: str = 'None', ASCII: str = 'None', tour_ID: str = 'None',
                tournaments: int = 0, wins: int = 0, runner_up: int = 0):
        
        self.name: str = name
        self.captain: str =  captain
        self.club: str = club
        self.web_link: str = web_link
        self.ASCII: str = ASCII
        self.tournament: int = tournaments
        self.wins: int = wins
        self.tour_ID: list = tour_ID
        self.runner_up: list = runner_up

    def team_to_csv(self) -> list:
        '''Tourns Team into list of values for easy csv handeling'''

        return [self.name, self.captain, self.club, self.web_link,
                self.ASCII, self.tour_ID, self.tournament, self.wins, self.runner_up]


    def __str__(self) -> str:
        '''Gives a formatted table of Team info'''


        return (

            f"{"☰"*84}\n"
            f"║ {self.name:^80} ║\n"
            f"║ {"┄"*80} ║\n"
            f"║ {" "*80} ║\n"
            f"║ {"Team captain:":<40}{self.captain:>40} ║\n"
            f"║ {"Club:":<40}{self.club:>40} ║\n"
            f"║ {"Team's ASCII logo:":<40}{self.ASCII:>40} ║\n"
            f"║ {"Tournaments played in":<40}{self.tournament:>40} ║\n"
            f"║ {"Wins:":<40}{self.wins:>40} ║\n"
            f"║ {" "*80} ║\n"
            f"║{self.web_link:^80} ║\n"
            f"{"☰"*84}"
            )
