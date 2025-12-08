from typing import List
from models.player import Player

class Team:
    name: str
    captain: str
    web_link: str
    ASCII = str

    def __init__(self, name: str, captain: str, club: str = 'None',
                web_link: str = 'None', ASCII: str = 'None', tour_IDs: str = 'None',
                tournaments: int = 0, wins: int = 0, runner_up: int = 0):
        
        self.name: str = name
        self.captain: str =  captain
        self.club: str = club
        self.web_link: str = web_link
        self.ASCII: str = ASCII
        self.tournament: int = tournaments
        self.wins: int = wins
        self.tour_IDs: list = tour_IDs.split()

        self.players: List[Player] = []

    
    
    def team_to_csv(self) -> list:
        self.tour_IDs = " ".join(self.tour_IDs)
        return [self.name, self.captain, self.club, self.web_link,
                self.ASCII, self.tour_IDs, self.tournament, self.wins]


    def __str__(self) -> str:
        # User-facing print
        return (

            f"Team name: [{self.name}] \n"
            f"Team captain: [{self.captain}] \n "
            f"Club: [{self.club}] \n"
            f"Team's link to web page [{self.web_link}] \n"
            f"Team's ASCII logo: [{self.ASCII}] \n"
            f"Team has played in {self.tournament} tournaments \n"
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