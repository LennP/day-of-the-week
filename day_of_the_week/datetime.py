"""Datetime day-of-the-week algorithm."""

from datetime import datetime
from enum import IntEnum


class Weekday(IntEnum):
    """Day of the week."""

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    return Weekday(date.weekday())
