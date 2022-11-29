import pytest
import datetime
import sys
import consts
from model import Individual, Family
from validator import check_US18

def sibs_should_not_marry(capfd):
    i1 = Individual("I01", "A", "M", gedcom_date_to_datetime("1 JAN 2022"))
    i2 = Individual("I02", "A", "M", gedcom_date_to_datetime("1 AUG 2022"))
    i3 = Individual("I03", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))
    i4 = Individual("I04", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))


    family = Family("F01", i1, i2, [], None, None)
    family.set_children([i3, i4])

    family2 = Family("F02", i3, i4, [], None, None)
    i3.set_fams(family2.id)
    i4.set_fams(family2.id)

    check_US18(family)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US18.format(i3)