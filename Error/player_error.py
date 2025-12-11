

class PlayerEmptyInputError(Exception):
    '''Raise if input is empty'''
    pass

class TooYoungError(Exception):
    """Raise if player is too youngr"""
    pass

class TooOldError(Exception):
    '''Raise if player is too old'''
    pass

class InvalidAgeException(Exception):
    """Raise if age is not in the correct format"""
    pass

class InvalidEmailException(Exception):
    """Raise if Email necessary"""
    pass

class invalidNumberException(Exception):
    '''Raise if phone number is invalid'''
    pass

class InvalidCharacterHandle(Exception):
    """Raise if invalid characters are in handle"""
    pass

class InvaldlinkException(Exception):
    '''Raise if link is invalid'''
    pass

class HandleExistsException(Exception):
    """Raise if handle is already in use"""
    pass

class InvalidLinkException(Exception):
    '''Raise if link is invalid'''
    pass

class InvalidNumberException(Exception):
    '''Raise if number is invalid'''
    pass
class PlayerNotExist(Exception):
    '''Raise if Player does not exisst'''


    