import pytest
import datetime
import sys
import consts
from model import Individual, Family
from util import gedcom_date_to_datetime
from validator import check_US18

#couldn't rename it but test for sibling being married
def test_more_than_five_births(capfd):
    i1 = Individual("I01", "A", "M", gedcom_date_to_datetime("1 JAN 2022"))
    i2 = Individual("I02", "A", "M", gedcom_date_to_datetime("1 AUG 2022"))
    i3 = Individual("I03", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))
    i4 = Individual("I04", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))

    i5 = Individual("I05", "A", "M", gedcom_date_to_datetime("1 JAN 2022"))
    i6 = Individual("I06", "A", "M", gedcom_date_to_datetime("1 AUG 2022"))
    i7 = Individual("I07", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))
    i8 = Individual("I08", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))
    i9 = Individual("I09", "A", "M", gedcom_date_to_datetime("2 AUG 2022"))


    family = Family("F01", i1, i2, [], None, None)
    family.set_children([i3, i4])

    family2 = Family("F02", i3, i9, [], None, None)
    i3.set_fams(family2.id)
    i9.set_fams(family2.id)

    family3 = Family("F03", i5, i6, [], None, None)
    family3.set_children([i7, i8])

    family4 = Family("F04", i7, i8, [], None, None)
    i7.set_fams(family4.id)
    i8.set_fams(family4.id)

    check_US18([family, family2, family3, family4])
    out, err = capfd.readouterr()
    #print(out.strip())
    assert out.strip() == consts.MSG_US18.format(i8.id)
