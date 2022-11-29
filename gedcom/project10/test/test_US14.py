import pytest
import datetime
import sys
import consts
from model import Individual, Family
from validator import check_US14

#should print out anomaly message , there are 6 siblings with the same birth
def test_more_than_five_births(capfd):
    mom = Individual("I01", datetime.datetime(1999, 10, 12) + datetime.timedelta(days=1))
    dad = Individual("I02", datetime.datetime(1997, 1, 12) + datetime.timedelta(days=1))


    sib1 = Individual("I03", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib2 = Individual("I04", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib3 = Individual("I05", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib4 = Individual("I06", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib5 = Individual("I07", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib6 = Individual("I08", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))


    obj = Family("F01", mom, dad, [], datetime.datetime(2001, 1, 2) + datetime.timedelta(days=1))
    obj.set_children([sib1, sib2, sib3, sib4, sib5, sib6])

    #print(sib1.birth)
    
    check_US14(obj)
    out, err = capfd.readouterr()
    #print(out.strip())
    assert out.strip() == consts.MSG_US14.format(str(obj.id))

    #should not print out anomaly message , there are 4 siblings with the same birth
def test_less_than_five_births(capfd):
    mom = Individual("I01", datetime.datetime(1999, 10, 12) + datetime.timedelta(days=1))
    dad = Individual("I02", datetime.datetime(1997, 1, 12) + datetime.timedelta(days=1))


    sib1 = Individual("I03", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib2 = Individual("I04", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib3 = Individual("I05", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib4 = Individual("I06", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))

    obj = Family("F01", mom, dad, [], datetime.datetime(2001, 1, 2) + datetime.timedelta(days=1))
    obj.set_children([sib1, sib2, sib3, sib4])

    #print(sib1.birth)
    
    check_US14(obj)
    out, err = capfd.readouterr()
    #print(out.strip())
    assert out.strip() == "" #nothing should print

#exactly 5 siblings should not print out message
def test_five_births(capfd):
    mom = Individual("I01", datetime.datetime(1999, 10, 12) + datetime.timedelta(days=1))
    dad = Individual("I02", datetime.datetime(1997, 1, 12) + datetime.timedelta(days=1))


    sib1 = Individual("I03", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib2 = Individual("I04", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib3 = Individual("I05", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib4 = Individual("I06", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    sib5 = Individual("I07", datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))


    obj = Family("F01", mom, dad, [], datetime.datetime(2001, 1, 2) + datetime.timedelta(days=1))
    obj.set_children([sib1, sib2, sib3, sib4, sib5])

    #print(sib1.birth)
    
    check_US14(obj)
    out, err = capfd.readouterr()
    #print(out.strip())
    assert out.strip() == "" #nothing should print

