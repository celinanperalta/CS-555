import pytest
import datetime
from src.parse import reject_invalid_date
from src.util import gedcom_date_to_datetime


def test_invalid_date1():
    assert reject_invalid_date("31 FEB 2022")

def test_invalid_date2():
    assert reject_invalid_date("1 MAR 1999")

def test_invalid_date3():
    assert reject_invalid_date("40 DEC 2023")

def test_invalid_date4():
    assert reject_invalid_date("2 JUN 2001")

def test_invalid_date5():
    assert reject_invalid_date("31 APR 2005")
