"""Datetime day-of-the-week algorithm."""

from datetime import datetime

from day_of_the_week.models import Weekday


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    return Weekday(date.isoweekday() % 7)


if __name__ == "__main__":

    print(
        "1st of January 2001 is a",
        date_to_day_of_week(datetime(year=2001, month=1, day=1)).name.title(),
    )
    print("Today is a", date_to_day_of_week(datetime.now()).name.title())
