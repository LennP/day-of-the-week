"""Rata Die day-of-the-week algorithm."""

from datetime import datetime

from day_of_the_week.models import Weekday


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    day_of_the_week = (
        (
            date
            - datetime(year=1, month=1, day=1)
        ).days
        + 1
    ) % 7

    return Weekday(day_of_the_week)


if __name__ == "__main__":

    print(
        "1st of January 2001 is a",
        date_to_day_of_week(datetime(year=2001, month=1, day=1)).name.title(),
    )
    print("Today is a", date_to_day_of_week(datetime.now()).name.title())
