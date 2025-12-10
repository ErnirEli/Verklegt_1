class Club:
    name: str
    color: str
    hometown: str
    country: str
    
    def __init__(self, name: str, color: str, hometown: str, country: str, tournaments: str = 0, wins: str = 0):
        self.name = name
        self.color = color
        self.hometown = hometown
        self.country = country
        self.tournaments = tournaments
        self.wins = wins


    def club_to_csv(self) -> list:
        return [self.name, self.color, self.hometown, self.country, self.tournaments, self.wins]
    
    def __str__(self) -> str:
        return (
            f"Club name: [{self.name} \n"
            f"club color: [{self.color}] \n"
            f"Club hometown: [{self.hometown}] \n"
            f"Club country: [{self.country}] \n"
            f"Club has played in [{self.tournaments}] tournamnets\n"
            f"Club has won [{self.wins}] tournamnts"
        )