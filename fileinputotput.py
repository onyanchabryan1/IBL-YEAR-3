name=input("what is your name? ")

with open("name.txt", "a") as file:
    file.write(f"{name}\n")