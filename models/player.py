
class Player:


    def __init__(self,name, dob, address, phone, 
                email, link, handle, team_name = "None", 
                tournament = 0, wins = 0, runner_up = 0):
        
        self.handle = handle
        self.name = name
        self.dob = dob
        self.address = address
        self.phone = phone
        self.email = email
        self.link = link
        self.team_name = team_name
        self.tournaments = tournament
        self.wins = wins
        self.runner_up = runner_up

    def player_to_csv(self):
        '''Turns a player into a list of values for easy csv handeling'''

        parts = [
            self.name,
            self.dob,
            self.address,
            self.phone,
            self.email,
            self.link,
            self.handle,
            self.team_name,
            self.tournaments,
            self.wins,
            self.runner_up,
            ]
        
        return parts

