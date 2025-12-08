import csv
from models.match import Match


class MatchFiles():
    FILE_NAME: str = "Datalayer\csv_files\match_file.csv"


    def write_match(self, matches: list):
        '''Takes in a list of matches, of type "Match",
        rewrites the match file with all matches in the list'''

        with open(self.FILE_NAME, "w", encoding = "utf-8", newline = "") as file:
            writer = csv.writer(file)

            for match in matches:
                match: Match

                csv_match: list = match.match_to_csv()
                writer.writerow(csv_match)


    def add_match(self, match: Match):
        '''Takes in a match, of type "Match",
        adds the match to the bottom of match file'''

        with open(self.FILE_NAME, "a", encoding = "utf-8", newline = "") as file:
            file_writer = csv.writer(file)

            csv_match: list = match.match_to_csv()
            file_writer.writerow(csv_match)


    def read_match(self) -> list:
        '''Returns a list of all matches in match file,
        matches are of type "Match"'''

        try:
            with open(self.FILE_NAME, "r", encoding = "utf-8") as file:
                file_reader = csv.reader(file)
                matches: list = []

                for match_info in file_reader:
                    match_info: list

                    match_number: int = int(match_info[0])
                    tournament_id: str = match_info[1]
                    round: str = match_info[2]
                    team_a: str = match_info[3]
                    team_b: str = match_info[4]
                    date: str = match_info[5]
                    time: str = match_info[6]
                    server: str = match_info[7]
                    a_score: int = int(match_info[8])
                    b_score: int = int(match_info[9])
                    winner: str = match_info[10]
                    state: bool = (match_info[11] == "True")

                    matches.append(Match(match_number, tournament_id, round,
                                        team_a, team_b,
                                        date, time, server, a_score,
                                        b_score, winner, state))

                return matches
            
        except FileNotFoundError:
            return []