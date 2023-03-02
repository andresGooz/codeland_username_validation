import re


def codeland_username_validation(username):
    if len(username) < 4 or len(username) > 25:
        return False
    if not re.match(r"^[a-zA-Z]$", username[0]):
        return False
    if not re.match(r"^[a-zA-Z0-9_]*$", username):
        return False
    if username[-1] == "_":
        return False
    return True


print(codeland_username_validation("aa_"))  # Output: False
print(codeland_username_validation("u__hello_world123"))  # Output: True
