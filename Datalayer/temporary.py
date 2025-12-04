class Player():
    def __init__(self, name, birthdate, home, phone, mail, link, handle, team = "None", tournaments = 0, wins = 0):
        self.name: str = name
        self.birthdate: str = birthdate
        self.home: str = home
        self.phone: str = phone
        self.mail: str = mail
        self.link: str = link
        self.handle: str = handle
        self.team: str = team
        self.tournaments: int = tournaments
        self.wins: int = wins


    def player_to_csv(self):
        return [self.name, self.birthdate, self.home, 
                self.phone, self.mail, self.link, 
                self.handle, self.team, 
                self.tournaments, self.wins]
    
class Team():
    def __init__(self, name: str, captain: str, link: str = "None", logo: str = "None"):
        self.name = name
        self.captain = captain
        self.link = link
        self.logo = logo

    def team_to_csv(self):
        return [self.name, self.captain, self.link, self.logo]