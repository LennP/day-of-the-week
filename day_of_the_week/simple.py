"""Simple day-of-the-week algorithm."""

from datetime import datetime
from enum import IntEnum


class Weekday(IntEnum):
    """Day of the week."""

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


DECADE_VALUES = [0, 5, 3, 1]
MONTH_VALUES = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]


def is_leap_year(year):
    """Determine if the given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    # Step 1: Decade
    total = DECADE_VALUES[(date.year // 100) % 4]

    # Step 2: Modulo decade
    year_modulo_decade = date.year % 100
    total += year_modulo_decade + year_modulo_decade // 4

    # Step 3: Year
    if is_leap_year(date.year) and date.month < 3:
        total -= 1

    # Step 4: Month
    total += MONTH_VALUES[date.month - 1]

    # Step 5: Day
    total += date.day

    # Step 6: Calculate the day of the week
    day_of_week = total % 7

    return Weekday(day_of_week)


if __name__ == "__main__":

    print(
        "1st of January 2001 is a",
        date_to_day_of_week(datetime(year=1, month=1, day=1)).name.title(),
    )
    print("Today is a", date_to_day_of_week(datetime.now()).name.title())


# def date_to_day_of_week(date: datetime) -> Weekday:
#     y = date.year
#     m = date.month
#     d = date.day

#     if m < 3:
#         m += 12
#         y -= 1

#     t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
#     v = (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) % 7

#     return Weekday((v + 5) % 7)  # Adjusted to start week from Monday
