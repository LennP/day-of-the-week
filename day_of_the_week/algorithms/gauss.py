"""Gauss' day-of-the-week algorithm."""

from datetime import datetime

from day_of_the_week.models import Weekday
from day_of_the_week.util import is_leap_year

MONTH_OFFSET = {
    0: [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5],  # normal years
    1: [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6],  # leap years
}


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    day_of_the_week = (
        6 * ((date.year - 1) % 400)
        + 4 * ((date.year - 1) % 100)
        + 5 * ((date.year - 1) % 4)
        + MONTH_OFFSET[int(is_leap_year(date.year))][date.month - 1]
        + date.day
    ) % 7

    return Weekday(day_of_the_week)


if __name__ == "__main__":

    print(
        "1st of January 2001 is a",
        date_to_day_of_week(datetime(year=2001, month=1, day=1)).name.title(),
    )
    print("Today is a", date_to_day_of_week(datetime.now()).name.title())
