
def value(greeting):
    """
    Get the value of a greeting based on the starting word.

    Args:
        greeting (str): The greeting string.

    Returns:
        int: The value of the greeting. 0 if greeting starts with "hello", 20 if it starts with "h"
            (but not "hello"), and 100 otherwise.

    """
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def main():
    greeting = input("Enter a greeting: ")
    greeting_value = value(greeting)
    print(f"The value of the greeting is: {greeting_value}")


if __name__ == "__main__":
    main()

from bank import value

# Test value function
def test_value():
    assert value("Hello, World!") == 0
    assert value("Happiness is the key to success.") == 20
    assert value("Good morning!") == 100
    assert value("hello, world!") == 0
    assert value("happiness is the key to success.") == 20
    assert value("GOOD MORNING!") == 100

    # Test with leading spaces
    assert value("   hello, world!") == 0
    assert value("   Happiness is the key to success.") == 20
    assert value("   Good morning!") == 100

    # Test with invalid input
    assert value("") == 100
    assert value("   ") == 100
