import pytest
import datetime
import sys
sys.path.append("..")
sys.path.append("../project06/src")
import consts
from model import Individual, Family
from validator import check_US14

def test_more_than_five_births(capfd):
    mom = Individual("I01", datetime.datetime(1999, 10, 12) + datetime.timedelta(days=1))
    dad = Individual("I02", datetime.datetime(1997, 1, 12) + datetime.timedelta(days=1))


    sib1 = Individual("I03", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib2 = Individual("I04", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib3 = Individual("I05", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib4 = Individual("I06", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib5 = Individual("I07", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib6 = Individual("I08", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))

    obj = Family("F01", mom, dad, [sib1, sib2, sib3, sib4, sib5, sib6], datetime.datetime.now() + datetime.timedelta(days=1))
    check_US14(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US14.format(str(obj.id))