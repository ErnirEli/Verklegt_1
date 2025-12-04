
class Player:


    def __init__(self, handle, name, dob, address,
                 phone, email, link, team_name):
        self.handle = handle
        self.name = name
        self.dob = dob
        self.address = address
        self.phone = phone
        self.email = email
        self.link = link
        self.team_name = team_name

    def to_line(self):
        parts = [
            self.handle,
            self.name,
            self.dob,
            self.address,
            self.phone,
            self.email,
            self.link,
            self.team_name,
        ]
        return ";".join(parts)

