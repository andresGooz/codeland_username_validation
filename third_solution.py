import re


def check_username_length(username: str):
    if len(username) < 4 or len(username) > 25:
        return False
    return True


def check_username_start(username: str):
    if not re.match(r"^[a-zA-Z]*$", username[0]):
        return False
    return True


def check_username_characters(username: str):
    if not re.match(r"^[a-zA-Z0-9_]*$", username):
        return False
    return True


def check_username_underscore_end(username: str):
    if username[-1] == "_":
        return False
    return True


def codeland_username_validation(username: str):
    if (
        check_username_length(username)
        and check_username_start(username)
        and check_username_characters(username)
        and check_username_underscore_end(username)
    ):
        return True
    else:
        return False


input_string = input("Your word: ")
print(codeland_username_validation(input_string))
