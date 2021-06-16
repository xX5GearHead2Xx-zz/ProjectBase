import re


def ValidateEmail(email):
    email_pattern = ".+\@.+\..+"
    return bool(re.fullmatch(email_pattern, email))


def ValidatePassword(string):
    password_pattern = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$"
    return bool(re.fullmatch(password_pattern, string))
