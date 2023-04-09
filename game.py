# The code is a simple guessing game where the user is prompted to enter a level and then guess a
# randomly generated number within that level. The `import random` statement imports the random
# library which is used to generate the random number. The `while True` loops are used to keep the
# program running until the user correctly guesses the number. The `try` and `except` statements are
# used to handle errors that may occur during user input.
import random#import random library
while True:#loop the code forever
    try:#try code for errors
        level=int(input("Enter level: "))#prompt user for level
        if level>0:
            break

    except:#exception if error found
        pass#prompt user again

random_number=random.randint(1,level)
while True:
    try:
        guess=int(input("guess: "))#prompt user for guess input
        if guess>0:#condition
            if guess<random_number:
                print("too small")
            elif guess>random_number:
                print("Too large")
            else:
                print("Just roght!!")
    except:
        pass