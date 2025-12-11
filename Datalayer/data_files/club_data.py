import csv
from models.club import Club


class ClubFiles():
    FILE_NAME = "Datalayer\csv_files\club_file.csv"


    def write_club(self, clubs: list):
        '''Takes in a list of clubs, of type "Club"
        rewrites the club file with all clubs in the list'''

        with open(self.FILE_NAME, "w", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            for club in clubs:
                club: Club

                csv_club = club.club_to_csv()
                file_writer.writerow(csv_club)


    def add_club(self, club: Club):
        '''Takes in a club, of type "Club",
        adds the club to the bottom of club file'''

        with open(self.FILE_NAME, "a", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            csv_club = club.club_to_csv()
            file_writer.writerow(csv_club)


    def read_club(self) -> list:
        '''Returns a list of all clubs in club file,
        clubs are of type "Club"'''

        try:
            with open(self.FILE_NAME, "r", encoding = "utf-8") as file:
                file_reader = csv.reader(file)
                clubs = []

                for club_info in file_reader:
                    club_info: list
                    name: str = club_info[0]
                    colors: str = club_info[1]
                    town: str = club_info[2]
                    country: str = club_info[3]
                    tournaments: int = int(club_info[4])
                    wins: int = int(club_info[5])
                    runner_up = int(club_info[6])
                    
                    clubs.append(Club(name, colors, town, country,
                                    tournaments, wins, runner_up))
                    
                return clubs
            
        except FileNotFoundError:
            return []