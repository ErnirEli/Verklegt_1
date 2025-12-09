class EmptyInput:
    '''Raise if input is empty'''
    pass

class InvalidStartDateInPast:
    '''Raise if start date is in the past'''
    pass
class InvalidStartDateBefore:
    '''Raise if start date is before end date'''
    pass

class InvalidContactEmail:
    '''Raise if the contact persons email is invalid'''
    pass
class InvalidContactNumber:
    '''Raise if the contact persons phone number is invalid'''
    pass

class WrongNumOfTeams:
    '''Raise if tournament has less than 16 teams or more than 64 teams'''
    pass

class TeamAlreadyInTournament:
    '''Raise if inputed team is already in tournament'''
    pass
class TeamDoesNotExist:
    '''raise if a inputed team to tournament does not exist'''
    pass

class IdAlreadyExists:
    '''Raise if inputed id already exists'''
    pass
class InvalidServers:
    '''Raise if number of servers are not betwenn 1-9'''