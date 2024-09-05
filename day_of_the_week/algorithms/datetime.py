"""Datetime day-of-the-week algorithm."""

from datetime import datetime

from day_of_the_week.models import Weekday


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    return Weekday(date.weekday())
