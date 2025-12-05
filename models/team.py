from typing import List
from models.player import Player

class Team:
    name: str
    captain: str
    web_link: str
    ASCII = str

    def __init__(self,name: str, captain: str, web_link: str = None, ASCII: str = None, tournaments: int = 0, wins: int = 0):
        self.name = name
        self.captain =  captain
        self.web_link = web_link
        self.ASCII = ASCII
        self.tournament = tournaments
        self.wins = wins

        self.players: List[Player] = []

    #Ekki viss um að þurfi

<<<<<<< Updated upstream
    #def to_list(self) -> list[str, str]:
     #   return [self.name, self.captain, self.web_link, self.ASCII]
=======
    
    def team_to_csv(self) -> list:
        return [self.name, self.captain, self.web_link, self.ASCII, self.tournament, self.wins]
>>>>>>> Stashed changes
    


    def __str__(self) -> str:
        # User-facing print
        return (
            f"Team name: [{self.name}] "
            f"Team captain: [{self.captain}] "
            f"Team's link to web page [{self.web_link}] "
            f"Team's ASCII logo: [{self.ASCII}] "
            f"Team has played in {self.tournament} tournaments"
            f"Team has won {self.wins} tournaments"
        )


#Ekki viss um að þurfi

    # def __repr__(self) -> str:
    #     # Dev/debug print
    #     return (
    #         f"Team(name={self.name}"
    #         f"captain = {self.captain}"
    #         f"link to web page = {self.web_link}"
    #         f"ASCII logo = {self.ASCII}" 
    #     )