from Datalayer.data_api import DataAPI
from Datalayer.temporary import Team
from Datalayer.temporary import Player

print(""
"1. Bæta við player\n"
"2. Sýna alla players\n"
"3. Breyta einum leikmanni\n"
"4. Bæta við liði\n"
"5. Sýna öll lið\n"
"6. Breyta einu liði\n"
)

action = int(input())
files = DataAPI()
if action == 1:
    name = input("Name: ")
    birth = input("Birthdate: ")
    home = input("Home: ")
    phone = input("Phone: ")
    mail = input("Mail: ")
    link = input("Link: ")
    handle = input("Handle: ")

    player = Player(name, birth, home, phone, mail, link, handle)
    files.add_player(player)

if action == 2:
    players = files.get_all_players()
    if len(players) == 0:
        print("There are no players")
    for player in players:
        print(player.handle)

if action == 3:
    players = files.get_all_players()
    if len(players) == 0:
        print("There are no players")
    handle = input("Enter Player handle for change: ")
    for player in players:
        if handle == player.handle:
            print("Handle: ", player.handle)
            print("Team:   ", player.team)
            print("Link:   ", player.link)
            new_handle = input("new player handle: ")
            player.handle = new_handle
            print("Handle: ", player.handle)
            print("Team:   ", player.team)
            print("Link:   ", player.link)
            break
    files.rewrite_players(players)
    
if action == 4:
    name = input("Team name: ")
    captain = input("Team Captain: ")
    link = input("Link: ")
    logo = input("Ascii logo: ")
    if link == "":
        link = None
    if logo == "":
        logo = None

    team = Team(name, captain, link, logo)
    files.add_team(team)

if action == 5:
    teams = files.get_all_teams()
    for team in teams:
        print(team)

if action == 6:
    teams = files.get_all_teams()
    name = input("Team Name for change: ")
    for team in teams:
        if name == team.name:
            print("Name: ", team.name)
            new = input("New name: ")
            team.name = new
            print("New name:", team.name)

    files.rewrite_teams(teams)






