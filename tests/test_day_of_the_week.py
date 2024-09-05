"""Test day of the week algorithms."""

import importlib
import inspect
import logging
import os
from collections.abc import Callable
from datetime import datetime, timedelta
from enum import Enum

import pytest

_LOGGER = logging.getLogger(__name__)


def get_algorithms():
    """
    Dynamically imports all date_to_day_of_week functions from modules in the './day_of_the_week' directory.
    """
    algorithms = []
    directory = "./day_of_the_week"  # Relative path from the project root
    for file in os.listdir(directory):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]  # Remove the .py extension
            module = importlib.import_module(f"day_of_the_week.{module_name}")
            algorithms.append((module_name, module.date_to_day_of_week))
    return algorithms


ALGORITHMS = get_algorithms()


@pytest.mark.parametrize("module_name,date_to_day_of_week", ALGORITHMS)
class TestDayOfTheWeek:
    """Test day of the week."""

    MIN_DATE = datetime(year=1, month=1, day=1)
    MAX_DATE = datetime(year=9999, month=12, day=31)
    MAX_NUM_DAYS: int = (MAX_DATE - MIN_DATE).days
    DAYS_OF_THE_WEEK: list[str] = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    @classmethod
    def test_day_progression(
        cls, module_name: str, date_to_day_of_week: Callable[[datetime], type[Enum]]
    ) -> None:
        """Test day progression."""

        base_date = datetime(year=1, month=1, day=1)

        for i in range(cls.MAX_NUM_DAYS):
            test_date = base_date + timedelta(days=i)
            calculated_day = date_to_day_of_week(test_date)
            expected_day = cls.DAYS_OF_THE_WEEK[i % 7]

            assert str(calculated_day.name).lower() == expected_day.lower(), (
                f"""{module_name.title()} algorithm failed for date: {test_date}, """
                f"""expected {expected_day}, got {str(calculated_day.name).title()}"""
            )

        _LOGGER.info(
            "%s algorithm passed %s", module_name.title(), inspect.stack()[0][3]
        )

    @classmethod
    def test_performance(
        cls,
        module_name: str,
        date_to_day_of_week: Callable[[datetime], type[Enum]],
        benchmark,
    ) -> None:
        """Benchmark the performance of day progression algorithm."""

        def run_day_progression():
            for i in range(cls.MAX_NUM_DAYS):
                test_date = cls.MIN_DATE + timedelta(days=i)
                date_to_day_of_week(test_date)

        # Use the benchmark fixture to measure execution time
        benchmark(run_day_progression)

        _LOGGER.info("%s algorithm performance test completed", module_name.title())
