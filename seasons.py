import sys
"""
    The function calculates a person's age in minutes and converts it into a string of years, days,
    hours, and minutes.
"""
from datetime import datetime, date, timedelta


def main():
    date_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        sys.exit(1)

    today = date.today()
    age_in_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    age_in_minutes = int(round(age_in_years * 365.25 * 24 * 60))

    print(age_in_words(age_in_minutes))


def age_in_words(minutes):
    units = [
        ('year', 525600),
        ('day', 1440),
        ('hour', 60),
        ('minute', 1)
    ]

    words = []
    for unit, value in units:
        count = minutes // value
        if count > 0:
            words.append("{} {}".format(count, unit if count == 1 else unit + "s"))
            minutes -= count * value

    if not words:
        return "0 minutes"

    return " ".join(words)


if __name__ == "__main__":
    main()
