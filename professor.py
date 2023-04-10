import random
    """
    The function generates 10 addition problems with randomly generated integers based on the user's
    chosen level and prompts the user to input the correct answer, giving them three attempts before
    moving on to the next problem and displaying their final score out of 10.
    """


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "
        answer = None
        attempts = 0
        while attempts < 3:
            user_input = input(problem)
            try:
                answer = int(user_input)
            except ValueError:
                print("EEE")
            if answer is not None and answer == x + y:
                score += 1
                break
            else:
                print("EEE")
                attempts += 1
        if attempts == 3:
            print(f"{problem}{x+y}")
    print(f"Score: {score}/10")


def get_level():
    while True:
        user_input = input("Enter level (1, 2, or 3): ")
        if user_input in ["1", "2", "3"]:
            return int(user_input)


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
