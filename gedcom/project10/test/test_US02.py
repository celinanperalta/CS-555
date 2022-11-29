import pytest
import datetime
import consts
from model import Individual, Family
from validator import check_US02

def test_birth_before_marriage(capfd):
    obj = Individual(id="I01", birth = datetime.datetime(1960, 3, 6) + datetime.timedelta(days=1))
    obj2 = Family(id="F01", husband=obj, marriage_date = datetime.datetime(1990, 8, 9) + datetime.timedelta(days=1))
    check_US02(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US02.format(str(obj), obj.birth, obj2.marriage_date)


def test_valid_marriage(capfd):
    obj = Individual(id="I01", birth = datetime.datetime(1960, 1, 2) + datetime.timedelta(days=1))
    obj2 = Family(id="FO1", husband=obj, marriage_date=datetime.datetime(2000, 10, 1))
    check_US02(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US02.format(str(obj), obj.birth, obj2.marriage_date)

def test_birth_no_marriage(capfd):
    obj = Individual(id="I01", birth = datetime.datetime(2000, 12, 1) + datetime.timedelta(days=1))
    obj2 = Family(id="I01", husband=obj, marriage_date=None)
    check_US02(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_marriage_no_birth(capfd):
    obj = Individual(id="I01", birth=None)
    obj2 = Family(id="F01", husband=obj, marriage_date=datetime.datetime.now())
    check_US02(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_same_birth_same_marriage(capfd):
    obj = Individual(id="I01", birth = datetime.datetime(1999, 3, 20) + datetime.timedelta(days=1))
    obj2 = Family(id="F01", husband=obj, marriage_date = datetime.datetime(1999, 3, 20) + datetime.timedelta(days=1))
    check_US02(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US02.format(str(obj), obj.birth, obj2.marriage_date)
