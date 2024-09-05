"""Intermediate day-of-the-week algorithm."""

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


MONTH_VALUES: list[int] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    y = date.year
    y -= date.month < 3

    v = (
        y
        + y // 4
        - y // 100
        + y // 400
        + MONTH_VALUES[date.month - 1]
        + date.day
    ) % 7

    return Weekday(v)


if __name__ == "__main__":

    print(
        "1st of January 2001 is a",
        date_to_day_of_week(datetime(year=1, month=1, day=1)).name.title(),
    )
    print("Today is a", date_to_day_of_week(datetime.now()).name.title())
