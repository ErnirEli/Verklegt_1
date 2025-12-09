

class EmptyInput(Exception):
    """Raise if name is empty"""
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

class InvalidCharacterHandle(Exception):
    """Raise if invalid characters are in handle"""
    pass

class HandleExistsException(Exception):
    """Raise if handle is already in use"""
    pass

class InvalidLinkException(Exception):
    pass

class InvalidNumberException(Exception):
    pass

    