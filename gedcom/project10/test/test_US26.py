import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US26
from util import gedcom_date_to_datetime


def test_US26(capfd):

    
    i0 = Individual("I0", "Albert", "M", gedcom_date_to_datetime("2 JAN 2000"), None, [], [])
    i1 = Individual("I1", "Albert", "M", gedcom_date_to_datetime("1 JAN 2000"), None, [], [])
    i2 = Individual("I2", "Balbert", "M", gedcom_date_to_datetime("5 JAN 2000"), None, [], [])
    i3 = Individual("I3", "Balbert", "M", gedcom_date_to_datetime("3 JAN 2003"), None, [], [])

    family = Family("F01", None, None, [], None, None)
    family.set_children([i0, i1, i2])

    individuals = [i0, i1, i2, i3]

    for i in individuals:
        i.set_famc([family.id])

    check_US26([family], individuals)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US26.format(i3, "child", family)
