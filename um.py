def count(s):
    """
    The function counts the number of times the word "um" appears in a given string.
    
    :param s: a string that contains words to be counted
    :return: The function `count` returns the number of times the word "um" appears in a given string
    `s`.
    """
    # Split the string into words and convert them to lowercase
    words = s.lower().split()

    # Count the number of times "um" appears as a word
    um_count = sum(1 for word in words if word == "um")

    return um_count
