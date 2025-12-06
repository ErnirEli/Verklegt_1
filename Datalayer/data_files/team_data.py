import csv
from models.team import Team


class TeamFiles():
    FILE_NAME: str = "Datalayer\csv_files\\team_file.csv"


    def write_team(self, teams: list):
        '''Takes in a list of tems, of type "Team",
        rewrites the team file with all teams in the list'''

        with open(self.FILE_NAME, "w", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            for team in teams:
                team: list = team.team_to_csv()
                file_writer.writerow(team)


    def add_team(self, team: list):
        '''Takes in a team, of type "Team",
        adds the team to the bottom of team file'''

        with open(self.FILE_NAME, "a", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            csv_team: list = team.team_to_csv()
            file_writer.writerow(csv_team)


    def read_team(self):
        '''Returns a list of all tems in team file,
        teams are of type "Team"'''

        try:
            with open(self.FILE_NAME, "r", encoding = "utf-8", newline = "") as file:
                file_reader = csv.reader(file)
                teams = []
                for line in file_reader:
                    name: str = line[0]
                    captain: str = line[1]
                    club: str = line[2]
                    mail: str = line[3]
                    logo: str = line[4]
                    tour_IDs = line[5]
                    tournaments: int = int(line[6])
                    wins: int = int(line[7])

                    teams.append(Team(name, captain, club, mail,
                                    logo, tour_IDs, tournaments, wins))

                return teams
            
        except FileNotFoundError:
            return []
        



