import pytest
import datetime
import sys
sys.path.append("..")
sys.path.append("../project04/src")
import consts
from model import Individual, Family
from validator import check_US02

def test_birth_before_marriage(capfd):
    obj = Family(id="F01", husband="Sam", wife="Judy", birth = datetime.datetime.now() + datetime.timedelta(days=1), marriage_date=datetime.datetime.now())
    check_US02(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US02.format("Birth", obj.birth, obj.marriage_date)


def test_valid_marriage(capfd):
    obj = Family(id="FO1", husband="Herbert", wife="Sherbet", marriage_date=datetime.datetime.now(), birth = datetime.datetime.now() + datetime.timedelta(days=1))
    check_US02(obj)
    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_birth_no_marriage(capfd):
    obj = Family(id="I01", birth = datetime.datetime.now())
    check_US02(obj)
    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_marriage_no_birth(capfd):
    obj = Family(id="F01", husband="Max", wife="Ruby", marriage_date=datetime.datetime.now())
    check_US02(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US02.format(obj.wife, obj.husband, obj.birth, obj.marriage_date)

def test_empty(capfd):
    obj = Individual(id="I01")
    check_US02(obj)
    out, err = capfd.readouterr()
    assert out == ""
