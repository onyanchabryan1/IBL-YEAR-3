def validate(ip):
    """
    The function checks if a given string is a valid IPv4 address by splitting the string into its
    components and ensuring that each component is an integer between 0 and 255.
    
    :param ip: a string representing an IPv4 address to be validated
    :return: The function `validate` returns a boolean value indicating whether the input string is a
    valid IPv4 address or not. The `main` function calls the `validate` function with user input and
    prints the boolean result.
    """
    """
    Check if a given string is a valid IPv4 address.

    Args:
        ip (str): The IPv4 address string to validate.

    Returns:
        bool: True if the input string is a valid IPv4 address, False otherwise.

    """
    # Split the string into its components
    components = ip.split(".")

    # Ensure that there are exactly four components
    if len(components) != 4:
        return False

    # Ensure that each component is an integer between 0 and 255
    for component in components:
        try:
            if int(component) < 0 or int(component) > 255:
                return False
        except ValueError:
            return False

    # If all checks passed, the input is a valid IPv4 address
    return True


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
