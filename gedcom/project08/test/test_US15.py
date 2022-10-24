import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US15
from util import gedcom_date_to_datetime

'''
There should be fewer than 15 siblings in a family
'''

def test_has_15(capfd):

    children = []
    for i in range(0, 15):
        children.append(Individual("I" + str(i), "A", "M", gedcom_date_to_datetime("1 JAN " + str(2000 + i))))

    family = Family("F01", None, None, [], None, None)
    family.set_children(children)
    check_US15(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US15.format(family.id)
