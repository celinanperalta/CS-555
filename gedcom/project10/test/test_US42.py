import pytest
import datetime
from src.parse import reject_invalid_date
from src.util import gedcom_date_to_datetime


def test_invalid_date1():
    reject_invalid_date("31 FEB 2022")
    assert True

def test_invalid_date2():
    reject_invalid_date("1 MAR 1999")
    assert reject_invalid_date("1 MAR 1999")

def test_invalid_date3():
    reject_invalid_date("40 DEC 2023")
    assert True

def test_invalid_date4():
    reject_invalid_date("3 JUN 2001")
    assert reject_invalid_date("3 JUN 2001")

def test_invalid_date5():
    reject_invalid_date("31 APR 2005")
    assert True