import csv
from models import Tournament


class TournamentFiles():
    FILE_NAME = "Datalayer\csv_files\\tournament_file.csv"


    def write_tournament(self, tournaments: list):
        '''Takes in a list of tournaments, of type "Tournament",
        rewrites the tournament file with all tournaments in the list'''

        with open(self.FILE_NAME, "w", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            for tournament in tournaments:
                tournament: Tournament

                csv_tournament = tournament.tournament_to_csv()
                file_writer.writerow(csv_tournament)


    def add_tournament(self, tournament: Tournament):
        '''Takes in a tournament, of type "Tournament",
        adds the tournament to the bottom of the tournament file'''

        with open(self.FILE_NAME, "a", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            csv_tournament = tournament.tournament_to_csv()
            file_writer.writerow(csv_tournament)


    def read_tournament(self) -> list:
        '''Returns a list of all tournaments in tournament file,
        tournaments are of type "Tournament"'''

        try:
            with open(self.FILE_NAME, "r", encoding = "utf-8") as file:
                file_reader = csv.reader(file)
                tournaments: list = []

                for tournament_info in file_reder:
                    tournament_info: list

                    id: int = int(tournament_info[0])
                    name: str = tournament_info[1]
                    venue: str = tournament_info[2]
                    start_date: str = tournament_info[3]
                    end_date: str = tournament_info[4]
                    contact: str = tournament_info[5]
                    mail: str = tournament_info[6]
                    number: int = int(tournament_info[7])
                    servers: int = int(tournament_info[8])

                    tournaments.append(Tournament(id, name, venue,
                                                start_date, end_date, contact,
                                                mail, number, servers))
                
                return tournaments
        
        except FileNotFoundError:
            return []