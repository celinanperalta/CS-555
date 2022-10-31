import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US17
from util import gedcom_date_to_datetime

'''
Parents should not marry any of their descendants
'''

def test_descendant_marriage(capfd):
    i1 = Individual("I01", "A", "M", gedcom_date_to_datetime("1 JAN 2022"))
    i2 = Individual("I02", "A", "M", gedcom_date_to_datetime("1 AUG 2022"))
    i3 = Individual("I03", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))

    family = Family("F01", i1, i2, [], None, None)
    family.set_children([i3])

    family2 = Family("F02", i1, i3, [], None, None)

    check_US17([family, family2])

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US17.format(i1.id, i3.id)
