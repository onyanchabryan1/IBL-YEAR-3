from validators import validate_email
    """
    The function takes an email address as input and uses the `validate_email` function from the
    `validators` module to determine if the email is valid or not, and prints the result.
    """


def main():
    email = input("Enter an email address: ")
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
