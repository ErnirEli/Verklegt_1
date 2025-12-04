import csv
from Datalayer.temporary import Player
from Datalayer.team_data import TeamFiles
from Datalayer.temporary import Team

class PlayerFiles():
    FILE_NAME: str = "Datalayer\csv_files\player_file.csv"

    def write_player(self, players: list):
        with open(self.FILE_NAME, "w", encoding = "utf-8", newline = "") as file:
            for player in players:
                player: Player
                csv_player: list = player.player_to_csv()
                file_writer = csv.writer(file)
                file_writer.writerow(csv_player)

    def add_player(self, player: Player):
        with open(self.FILE_NAME, "a", encoding = "utf-8", newline = "") as file:
            csv_player: list = player.player_to_csv()
            file_writer = csv.writer(file)
            file_writer.writerow(csv_player)

    def read_player(self):
        try:
            with open(self.FILE_NAME, "r", encoding = "utf-8", newline = "") as file:
                file_reader = csv.reader(file)
                players: list = []
                for player_info in file_reader:
                    player_info: list
                    name: str = player_info[0]
                    birthdate: str = player_info[1]
                    home: str = player_info[2]
                    phone: str = int(player_info[3])
                    mail: str = player_info[4]
                    link: str = player_info[5]
                    handle: str = player_info[6]
                    team: str = player_info[7]
                    tournaments: int = int(player_info[8])
                    wins: int = int(player_info[9])
                    player: Player = Player(name, birthdate, home, phone, mail, link, handle, team, tournaments, wins)
                    players.append(player)
                return players
            
        except FileNotFoundError:
            print("ooofff")
            return []
                
