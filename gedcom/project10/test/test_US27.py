import pytest
import datetime
import consts
from model import Individual, Family
from util import gedcom_date_to_datetime, get_age_in_years

def test_US27(capfd):
    
    i0 = Individual("I0", "John Doe", "M", birth=datetime.datetime.now() - datetime.timedelta(years=28))

    age = get_age_in_years(i0)

    assert age == 28

