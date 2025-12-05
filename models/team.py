from typing import List
from models.player import Player

class Team:
    name: str
    captain: str
    web_link: str
    ASCII = str

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    def __init__(self,name: str, captain: str, club: str = None, web_link: str = None, ASCII: str = None, tournaments: int = 0, wins: int = 0):
=======
    def __init__(self,name: str, captain: str, web_link: str = None, ASCII: str = None, tournaments: int = 0, wins: int = 0):
>>>>>>> Stashed changes
=======
    def __init__(self,name: str, captain: str, web_link: str = None, ASCII: str = None, tournaments: int = 0, wins: int = 0):
>>>>>>> Stashed changes
        self.name = name
        self.captain =  captain
        self.club = club
        self.web_link = web_link
        self.ASCII = ASCII
        self.tournament = tournaments
        self.wins = wins

        self.players: List[Player] = []

    
    
    def team_to_csv(self) -> list:
        return [self.name, self.captain, self.web_link, self.ASCII, self.tournament, self.wins]
<<<<<<< Updated upstream
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    


    def __str__(self) -> str:
        # User-facing print
        return (
<<<<<<< Updated upstream
            f"Team name: [{self.name}] \n"
            f"Team captain: [{self.captain}] \n "
            f"Club: [{self.club}] \n"
            f"Team's link to web page [{self.web_link}] \n"
            f"Team's ASCII logo: [{self.ASCII}] \n"
            f"Team has played in {self.tournament} tournaments \n"
=======
            f"Team name: [{self.name}] "
            f"Team captain: [{self.captain}] "
            f"Team's link to web page [{self.web_link}] "
            f"Team's ASCII logo: [{self.ASCII}] "
            f"Team has played in {self.tournament} tournaments"
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
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