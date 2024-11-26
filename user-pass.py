import re
def is_valid_username(username):
    """Check if the username meets the criteria."""
    if len(username) < 4 or len(username) > 20:
        return False
    if not re.match(r'^[A-Za-z0-9!@#$%^&*(),.?:{}|<>]+$', username):
        return False
    return True

def is_valid_password(password):
    """Check if the password meets the criteria."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# Get username from user with validation
while True:
    username = input("Enter your desired username (4 to 20 characters, might include letters, numbers, and special characters): ")
    if is_valid_username(username):
        print("Username created successfully!")
        break  # Exit the loop if the username is valid
    else:
        print("Invalid input. Please ensure your username is between 8 and 20 characters and contains only allowed characters.")

# Get password from user with validation
while True:
    password = input("Enter your desired password (at least 8 characters, include letters, numbers, and special characters): ")
    if is_valid_password(password):
        print("Password created successfully!")
        break  # Exit the loop if the password is valid
    else:
        print("Password does not meet the criteria. Please try again.")