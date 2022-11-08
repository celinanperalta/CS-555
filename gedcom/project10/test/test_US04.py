import pytest
import datetime
import consts
from model import Individual, Family
from validator import check_US04


def test_divorce_before_marriage(capfd):
    obj = Family(id="F01", husband="Bob", wife="Jo", marriage_date=datetime.datetime.now() + datetime.timedelta(days=1), divorce_date=datetime.datetime.now())
    check_US04(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US04.format(obj.wife, obj.husband, obj.marriage_date, obj.divorce_date)
    
def test_divorce_no_marriage(capfd):
    obj = Family(id="F01", husband="Rob", wife="Josie", divorce_date=datetime.datetime.now())
    check_US04(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US04.format(obj.wife, obj.husband, obj.marriage_date, obj.divorce_date)
    
def test_valid_divorce(capfd):
    obj = Family(id="F01", husband="Bobby", wife="Joy", marriage_date=datetime.datetime.now(), divorce_date=datetime.datetime.now() + datetime.timedelta(days=1))
    check_US04(obj)
    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_marriage_no_divorce(capfd):
    obj = Family(id="F01", husband="Robbie", wife="Joe", marriage_date=datetime.datetime.now())
    check_US04(obj)
    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_empty(capfd):
    obj = Family(id="F01")
    check_US04(obj)
    out, err = capfd.readouterr()
    assert out == ""
