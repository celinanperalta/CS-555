import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US34
from util import gedcom_date_to_datetime


def test_US34_husband_older(capfd):

    h = Individual("I0", "H", "M", birth=gedcom_date_to_datetime("1 JAN 1960"))
    w = Individual("I1", "W", "F", birth=gedcom_date_to_datetime("1 JAN 2000"))

    family = Family("F01", h, w, [],marriage_date=gedcom_date_to_datetime("1 JAN 2025"), divorce_date=None)
    
    check_US34([family])

    out, err = capfd.readouterr()
    assert consts.MSG_US34.format("I0", "I1") in out.strip()

def test_US34_wife_older(capfd):

    h = Individual("I0", "H", "M", birth=gedcom_date_to_datetime("1 JAN 2000"))
    w = Individual("I1", "W", "F", birth=gedcom_date_to_datetime("1 JAN 1960"))

    family = Family("F01", h, w, [],marriage_date=gedcom_date_to_datetime("1 JAN 2025"), divorce_date=None)

    check_US34([family])

    out, err = capfd.readouterr()
    assert consts.MSG_US34.format("I1", "I0") in out.strip()
