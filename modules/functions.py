'Functions public'

import os
import re
from config import config


def validate_folder():
    """Validate if folder exists"""

    # validate if folder not exists
    if not os.path.exists(config["path_folder_results"]):

        # create folder
        os.makedirs(config["path_folder_results"])
        print(f"1. Folder report created: {config['path_folder_results']}")

    # folder exists
    else:
        print(f"1. Folder report exists: {config['path_folder_results']}")


def validate_input_email():
    """Validate input email"""

    while True:
        email = input("Enter email: ")

        # validate if email is empty
        if email.strip() == "":
            print("Email is required")

        # validate if email is valid
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print("Invalid email format. Please enter a valid email address.")

        # email is valid
        else:
            break

    return email


# if __name__ == "__main__":
#     validate_folder()
#     input_email = validate_input_email()
#     print(input_email)
