# This code is creating a grocery dictionary to keep track of the number of times an item is entered
# by the user. It prompts the user to enter an item and checks if it already exists in the dictionary.
# If it does, it increments the count by 1, otherwise it adds the item to the dictionary with a count
# of 1. The loop continues until the user enters an EOF (end of file) signal, at which point it prints
# out the items and their counts in alphabetical order.

grocery = {}  # initialize an empty dictionary
while True:
    try:
        item = input("Enter item: ")
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key],key.upper())
        break

