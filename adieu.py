# This code reads names from user input until the end of file (EOF) is reached, and stores them in a
# list called `names`. It then formats a farewell message based on the number of names in the list,
# and prints the message to the console. If there is only one name, the message will be "Adieu, adieu,
# to [name]". If there are two names, the message will be "Adieu, adieu, to [name1] and [name2]". If
# there are more than two names, the message will be "Adieu, adieu, to [name1], [name2], ..., and
# [nameN]".
names = []

# Read names from user input until EOF
while True:
    try:
        name = input().strip()
    except EOFError:
        break
    if name:
        names.append(name)

# Format farewell message based on number of names
if len(names) == 1:
    message = f"Adieu, adieu, to {names[0]}"
else:
    message = "Adieu, adieu, to "
    if len(names) == 2:
        message += f"{names[0]} and {names[1]}"
    else:
        message += ", ".join(names[:-1]) + f", and {names[-1]}"

print(message)
