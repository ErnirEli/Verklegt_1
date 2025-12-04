import csv
from data_API import Player
from read import TeamFiles
from data_API import Team

class PlayerFiles():

    def write_player(players: list):
        with open("player_file.csv", "w", encoding = "utf-8", newline = "") as file:
            for player in players:
                player: list = player.player_to_csv()
                file_writer = csv.writer(file)
                file_writer.writerow(player)

    def add_player(players: list):
        with open("player_file.csv", "a", encoding = "utf-8", newline = "") as file:
            for player in players:
                player: list = player.player_to_csv()
                file_writer = csv.writer(file)
                file_writer.writerow(player)

    def read_player():
        with open("player_file.csv", "r", encoding = "utf-8", newline = "") as file:
            file_reader = csv.reader(file)
            players = []
            for line in file_reader:
                print(line)
                player: Player = Player(line[0], line[1], line[2])
                players.append(player)
            return players
            



k = [["Ernir Elí Ellertsson", 21, "Noobmaster69", 
    3, 1],
    ["Hafþór Huginn", 19, "NPC", 
    9, 0]]
Ernir = []
for x in k:
    Ernir.append(Player(x[0], x[1], x[2]))

PlayerFiles.write_player(Ernir)

leikmenn = PlayerFiles.read_player()

Birna = Team("GoonSquad", [leikmenn[0].handle, leikmenn[1].handle])

TeamFiles.write_team([Birna])

TeamFiles.read_team()

