import csv
from models.player import Player


class PlayerFiles():
    FILE_NAME: str = "Datalayer\csv_files\player_file.csv"


    def write_player(self, players: list):
        '''Takes in a list of players, of type "Player",
        rewrites the player file with all players in the list'''

        with open(self.FILE_NAME, "w", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            for player in players:
                player: Player

                csv_player: list = player.player_to_csv()
                file_writer.writerow(csv_player)


    def add_player(self, player: Player):
        '''Takes in a player, of type "Player",
        adds the player to the bottom of player file'''

        with open(self.FILE_NAME, "a", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            csv_player: list = player.player_to_csv()
            file_writer.writerow(csv_player)


    def read_player(self):
        '''Returns a list of all players in player file,
        players are of type "Player"'''

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
                    runner_up: int = int(player_info[10])

                    players.append(Player(name, birthdate, home,
                                        phone, mail, link, handle,
                                        team, tournaments, wins, runner_up))
                    
                return players
            
        except FileNotFoundError:
            return []
                
