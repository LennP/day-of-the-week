"""Intermediate day-of-the-week algorithm."""

import math
from datetime import datetime

from day_of_the_week.models import Weekday
from day_of_the_week.util import is_leap_year

MONTH_VALUES: list[int] = [1, 12, 5, 2, 7, 4, 9, 6, 3, 8, 12, 10]


def date_to_day_of_week(date: datetime) -> Weekday:
    """Returns the day of the week for a given date."""

    d = date.day    # 1 - 31
    m = date.month  # 1 - 12
    y = date.year
    d_0 = MONTH_VALUES[m - 1]
    y_0 = y % 10
    y_1 = (y % 100 - y_0) // 10
    c = y // 100

    w = (d - d_0 + y_0 - y_1 + math.floor(y_0/4 - y_1/2) - 2 * (c % 4)) % 7
    if m == 1:
        w -= 1
    elif is_leap_year(y):
        w -= 2

    return Weekday(w)


if __name__ == "__main__":

    print(
        "1st of January 2001 is a",
        date_to_day_of_week(datetime(year=2001, month=1, day=1)).name.title(),
    )
    print("Today is a", date_to_day_of_week(datetime.now()).name.title())
