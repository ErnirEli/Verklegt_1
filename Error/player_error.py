

class EmptyInput(Exception):
    """Raise if input is empty"""
    pass

class WrongAgeException(Exception):
    """Raise if age gets caught by ValueError"""
    pass

class InvalidAgeException(Exception):
    """Raise if age is not in the valid range"""
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


    