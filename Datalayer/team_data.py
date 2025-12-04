import csv
from data_API import Team

class TeamFiles():

    def write_team(teams: list):
        with open("team_file.csv", "w", encoding = "utf-8", newline = "") as file:
            for team in teams:
                team: list = team.team_to_csv()
                file_writer = csv.writer(file)
                file_writer.writerow(team)

    def add_team(teams: list):
        with open("team_file.csv", "a", encoding = "utf-8", newline = "") as file:
            for team in teams:
                team: list = team.team_to_csv()
                file_writer = csv.writer(file)
                file_writer.writerow(team)

    def read_team():
        with open("team_file.csv", "r", encoding = "utf-8", newline = "") as file:
            file_reader = csv.reader(file)
            teams = []
            for line in file_reader:
                print(line)
                team: Team = Team(line[0], [line[1], line[2]])
                teams.append(team)

            return teams


