def dollars_to_float(d):
    """
    Convert a dollar amount string formatted as $##.## to a float.
    """
    return float(d.strip('$'))

def percent_to_float(p):
    """
    Convert a percentage string formatted as ##% to a float.
    """
    return float(p.strip('%')) / 100

def main():
    """
    Prompt the user for the cost of the meal and the tip percentage, and calculate the tip amount.
    """
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f} as a tip.")

if __name__ == "__main__":
    main()
