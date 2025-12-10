class Club:
    name: str
    color: str
    hometown: str
    country: str
    
    def __init__(self, name: str, colors: str, hometown: str, country: str,
                tournaments: int = 0, wins: int = 0, runner_up: int = 0):
        self.name = name
        self.color = color
        self.hometown = hometown
        self.country = country
        self.tournaments = tournaments
        self.wins = wins
        self.runner_up = runner_up


    def club_to_csv(self) -> list:
        '''Turns Club into list of values for easy CSV handeling'''
        
        return [self.name, self.colors, self.hometown, self.country,
                self.tournaments, self.wins, self.runner_up]
    
    def __str__(self) -> str:
        return (
            f"Club name: [{self.name} \n"
            f"club color: [{self.color}] \n"
            f"Club hometown: [{self.hometown}] \n"
            f"Club country: [{self.country}] \n"
            f"Club has played in [{self.tournaments}] tournamnets\n"
            f"Club has won [{self.wins}] tournamnts"
        )