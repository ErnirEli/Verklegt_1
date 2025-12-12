

class InvalidStartDateInPast(Exception):
    '''Raise if start date is in the past'''
    pass
class InvalidStartDateBefore(Exception):
    '''Raise if start date is before end date'''
    pass

class InvalidContactEmail(Exception):
    '''Raise if the contact persons email is invalid'''
    pass
class InvalidContactNumber(Exception):
    '''Raise if the contact persons phone number is invalid'''
    pass

class WrongNumOfTeams(Exception):
    '''Raise if tournament has less than 16 teams or more than 64 teams'''
    pass

class TeamAlreadyInTournament(Exception):
    '''Raise if inputed team is already in tournament'''
    pass
class TeamDoesNotExist(Exception):
    '''raise if a inputed team to tournament does not exist'''
    pass

class IdAlreadyExists(Exception):
    '''Raise if inputed id already exists'''
    pass
class InvalidServers(Exception):
    '''Raise if number of servers are invalid'''
    pass

class InvalidFormat(Exception):
    '''Raised if format for start and end date is wrong'''
    pass

class InvalidAmountOfDays(Exception):
    '''Raised if tournament has an invalid amount of days'''
    pass

class TournamentNotExistError(Exception):
    '''Raise if inputed tournament does not exist'''
    pass