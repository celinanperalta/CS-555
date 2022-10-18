import pytest
import datetime
import sys
sys.path.append("..")
sys.path.append("../project06/src")
import consts
from model import Individual, Family
from validator import check_US18

#should print out anomaly message , there are 6 siblings with the same birth
def test_more_than_five_births(capfd):
    mom = Individual("I01", datetime.datetime(1979, 10, 12) + datetime.timedelta(days=1))
    dad = Individual("I02", datetime.datetime(1977, 1, 12) + datetime.timedelta(days=1))


    sib1 = Individual("I03", datetime.datetime(2000, 6, 9) + datetime.timedelta(days=1))
    sib2 = Individual("I04", datetime.datetime(2005, 7, 11) + datetime.timedelta(days=1))


    obj = Family("F01", mom, dad, [], datetime.datetime(2001, 1, 2) + datetime.timedelta(days=1))
    obj.set_children([sib1, sib2])

    obj2 = Family("F02", sib1, sib2, datetime.datetime(2022, 1, 2) + datetime.timedelta(days=1))

    sib1.set_fams(obj2)
    sib2.set_fams(obj2)

    #print(sib1.birth)
    
    check_US18(obj)
    out, err = capfd.readouterr()
    print(out.strip())
    assert out.strip() == consts.MSG_US18.format((obj.children[1].id))