import pytest
import datetime
from src.parse import is_valid_date
from src.util import gedcom_date_to_datetime


def test_full_date():
    assert is_valid_date("8 JUN 2000")

def test_date_no_day():
    assert is_valid_date("JUN 2000")

def test_date_no_day_no_month():
    assert is_valid_date("2000")

def test_gedcom_date_1():
    assert gedcom_date_to_datetime("JUN 2000") == datetime.datetime(2000, 6, 1)

def test_gedcom_date_2():
    assert gedcom_date_to_datetime("2000") == datetime.datetime(2000, 1, 1)