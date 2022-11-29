import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US38
from util import gedcom_date_to_datetime


def test_US38_one_birth(capfd):

    i0 = Individual("I0", "H", "M", birth=datetime.datetime.now() + datetime.timedelta(days=1))
    i1 = Individual("I1", "W", "F", birth=datetime.datetime.now() - datetime.timedelta(days=1))

    individuals = [i0, i1]

    birthdays = check_US38(individuals)
    assert ["H", (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%m-%d')] in birthdays
    assert ["W", (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%m-%d')] not in birthdays
    assert len(birthdays) == 2

def test_US38_two_births(capfd):

    i0 = Individual("I0", "H", "M", birth=datetime.datetime.now() - datetime.timedelta(days=363))
    i1 = Individual("I1", "W", "F", birth=datetime.datetime.now() + datetime.timedelta(days=29))

    individuals = [i0, i1]

    birthdays = check_US38(individuals)
    assert ["H", (datetime.datetime.now() - datetime.timedelta(days=363)).strftime('%m-%d')] in birthdays
    assert ["W", (datetime.datetime.now() + datetime.timedelta(days=29)).strftime('%m-%d')] in birthdays
    assert len(birthdays) == 3

def test_US38_no_birth(capfd):

    i0 = Individual("I0", "H", "M", birth=datetime.datetime.now() - datetime.timedelta(days=1))
    i1 = Individual("I1", "W", "F", birth=datetime.datetime.now() - datetime.timedelta(days=29))

    individuals = [i0, i1]

    birthdays = check_US38(individuals)
    assert ["H", (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%m-%d')] not in birthdays
    assert ["W", (datetime.datetime.now() - datetime.timedelta(days=29)).strftime('%m-%d')] not in birthdays
    assert len(birthdays) == 1
