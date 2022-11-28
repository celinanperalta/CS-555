import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US39
from util import gedcom_date_to_datetime


def test_US39_one_anniversary(capfd):

    i0 = Individual("I0", "H", "M", birth=datetime.datetime.now() + datetime.timedelta(days=1))
    i1 = Individual("I1", "W", "F", birth=datetime.datetime.now() - datetime.timedelta(days=1))
    family1 = Family("F01", i0, i1, [],marriage_date=datetime.datetime.now() + datetime.timedelta(days=1), divorce_date=None)
    family2 = Family("F02", i0, i1, [],marriage_date=datetime.datetime.now() - datetime.timedelta(days=1), divorce_date=None)

    individuals = [i0, i1]
    families = [family1,family2]

    anniversaries = check_US39(families)
    assert ["H", "W", (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%m-%d')] in anniversaries
    assert ["H", "W", (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%m-%d')] not in anniversaries
    assert len(anniversaries) == 2

def test_US39_two_anniversaries(capfd):

    i0 = Individual("I0", "H", "M", birth=datetime.datetime.now() - datetime.timedelta(days=363))
    i1 = Individual("I1", "W", "F", birth=datetime.datetime.now() + datetime.timedelta(days=29))
    family1 = Family("F01", i0, i1, [],marriage_date=datetime.datetime.now() - datetime.timedelta(days=363), divorce_date=None)
    family2 = Family("F02", i0, i1, [],marriage_date=datetime.datetime.now() + datetime.timedelta(days=29), divorce_date=None)

    individuals = [i0, i1]
    families = [family1,family2]

    anniversaries = check_US39(families)
    assert ["H", "W", (datetime.datetime.now() - datetime.timedelta(days=363)).strftime('%m-%d')] in anniversaries
    assert ["H", "W", (datetime.datetime.now() + datetime.timedelta(days=29)).strftime('%m-%d')] in anniversaries
    assert len(anniversaries) == 3

def test_US39_no_anniversary(capfd):

    i0 = Individual("I0", "H", "M", birth=datetime.datetime.now() - datetime.timedelta(days=1))
    i1 = Individual("I1", "W", "F", birth=datetime.datetime.now() - datetime.timedelta(days=29))
    family1 = Family("F01", i0, i1, [],marriage_date=datetime.datetime.now() - datetime.timedelta(days=1), divorce_date=None)
    family2 = Family("F02", i0, i1, [],marriage_date=datetime.datetime.now() - datetime.timedelta(days=29), divorce_date=None)

    individuals = [i0, i1]
    families = [family1,family2]

    anniversaries = check_US39(families)
    assert ["H", "W", (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%m-%d')] not in anniversaries
    assert ["H", "W", (datetime.datetime.now() - datetime.timedelta(days=29)).strftime('%m-%d')] not in anniversaries
    assert len(anniversaries) == 1
