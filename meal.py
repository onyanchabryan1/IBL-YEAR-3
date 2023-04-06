def convert(time):
    """Converts a time string in 24-hour format to the corresponding number of hours as a float."""
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

def main():
    """Prompts the user for a time and outputs whether it's breakfast time, lunch time, or dinner time."""
    time_str = input("Enter a time in 24-hour format (e.g. 13:30): ")
    time = convert(time_str)
    
    if 7 <= time < 8:
        print("It's breakfast time!")
    elif 12 <= time < 13:
        print("It's lunch time!")
    elif 18 <= time < 19:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
































