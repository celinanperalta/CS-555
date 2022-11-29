import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US13
from util import gedcom_date_to_datetime

'''
Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
(twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''

def test_less_than_8(capfd):
    i1 = Individual("I01", "A", "M", gedcom_date_to_datetime("1 JAN 2022"))
    i2 = Individual("I02", "A", "M", gedcom_date_to_datetime("1 AUG 2022"))

    family = Family("F01", None, None, [], None, None)
    family.set_children([i1, i2])
    check_US13(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US13.format(i1, i2)

def test_twins(capfd):
    i1 = Individual("I01", "A", "M", gedcom_date_to_datetime("1 JAN 2022"))
    i2 = Individual("I02", "A", "M", gedcom_date_to_datetime("2 JAN 2022"))

    family = Family("F01", None, None, [], None, None)
    family.set_children([i1, i2])
    check_US13(family)

    out, err = capfd.readouterr()
    assert out.strip() == ""
