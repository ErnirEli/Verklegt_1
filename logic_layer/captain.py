class Captain:
    def __init__(self):
        print("Captain class running!")
class Cancel:
    def __init__(self):
        print("Cancel selected. Goodbye!")
class ViewTeams:
    def __init__(self):
        print("Vie teams class selected")
class SeeTournament:
    def __init__(self):
        print("see tournaments selected")
class SeeMatchSchedule:
    def __init__(self):
        print("match Schedule")
class SeeMatchResult:
    def __init__(self):
        print("Seeing Match Result")
class ChangeRole:
    def __init__(self):
        print("Changing role")
class Createaplayer:
    def __init__(self):
        print("Create a player")
class addplayer:
    def __init__





class Captain():
    def __init__ (self):
        # Choice --> Class
        self.options = {
            "1": ViewTeams,
            "2": SeeTournament,
            "3": SeeMatchSchedule,
            "4": Createaplayer,
            "9": ChangeRole,
        } 

    def __str__(self):
        return 
    

class TeamLL:
    def __init__(self):
        self.teams = []

    def create_team(self, name, captain, url="" players = None):
        if players is None:
            players = []

        team = {
            "name" : name,
            "captain" : captain,
            "url": url,
            "players": players,
            "wins" : 0,
            "losses" : 0,
        }
        self.append.team(team)
        return team
    
    def edit_team_info(self, team_name 


    

    





        



