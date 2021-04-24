from re import match

def validNumber(phoneNumber):
    return bool(match('^\\(\\d{3}\\)\\s\\d{3}-\\d{4}$', phoneNumber))
