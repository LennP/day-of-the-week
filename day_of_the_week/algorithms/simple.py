"""Simple day-of-the-week algorithm."""

from datetime import datetime

from day_of_the_week.models import Weekday
from day_of_the_week.util import is_leap_year

DECADE_VALUES: list[int] = [0, 5, 3, 1]
MONTH_VALUES: list[int] = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    day_of_the_week = (
        DECADE_VALUES[(date.year // 100) % 4]
        + (date.year % 100 + (date.year % 100) // 4)
        + MONTH_VALUES[date.month - 1]
        + date.day
        - (1 if is_leap_year(date.year) and date.month < 3 else 0)
    ) % 7

    return Weekday(day_of_the_week)


if __name__ == "__main__":

    print(
        "1st of January 2001 is a",
        date_to_day_of_week(datetime(year=2001, month=1, day=1)).name.title(),
    )
    print("Today is a", date_to_day_of_week(datetime.now()).name.title())
