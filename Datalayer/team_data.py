import csv
from Datalayer.temporary import Team

class TeamFiles():
    FILE_NAME: str = "Datalayer\csv_files\\team_file.csv"

    def write_team(self, teams: list):
        with open(self.FILE_NAME, "w", encoding = "utf-8", newline = "") as file:
            for team in teams:
                team: list = team.team_to_csv()
                file_writer = csv.writer(file)
                file_writer.writerow(team)

    def add_team(self, team: list):
        with open(self.FILE_NAME, "a", encoding = "utf-8", newline = "") as file:
            team: list
            csv_team: list = team.team_to_csv()
            file_writer = csv.writer(file)
            file_writer.writerow(csv_team)

    def read_team(self):
        try:
            with open(self.FILE_NAME, "r", encoding = "utf-8", newline = "") as file:
                file_reader = csv.reader(file)
                teams = []
                for line in file_reader:
                    name: str = line[0]
                    captain: str = line[1]
                    mail: str = line[2]
                    logo: str = line[3]

                    team: Team = Team(name, captain, mail, logo)
                    teams.append(team)

                return teams
            
        except FileNotFoundError:
            return []
        



