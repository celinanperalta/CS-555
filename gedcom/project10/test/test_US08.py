import pytest
import datetime
import consts
from model import Individual, Family
from validator import check_US08

def test_birth_before_marriage(capfd):
    obj = Individual(id = "I01", birth = datetime.datetime(2020, 6, 9) + datetime.timedelta(days=1))
    obj2 = Family(id="F01", marriage_date = datetime.datetime(2020, 8, 17) + datetime.timedelta(days=1),divorce_date=datetime.datetime(2020, 9, 10)+ datetime.timedelta(days=1))
    obj2.add_child(obj)
    check_US08(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US08.format(str(obj), obj.birth, obj2.marriage_date)

def test_birth_after_9(capfd):
    obj = Individual(id = "I01", birth = datetime.datetime(2021, 6, 9) + datetime.timedelta(days=1))
    obj2 = Family(id="F01", marriage_date = datetime.datetime(2019, 8, 17) + datetime.timedelta(days=1),divorce_date=datetime.datetime(2019, 9, 10)+ datetime.timedelta(days=1))
    obj2.add_child(obj)
    check_US08(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US08.format(str(obj), obj.birth, obj2.divorce_date)

def test_birth_in_9(capfd):
    obj = Individual(id = "I01", birth = datetime.datetime(2019, 11, 12) + datetime.timedelta(days=1))
    obj2 = Family(id="F01", marriage_date = datetime.datetime(2019, 8, 17) + datetime.timedelta(days=1),divorce_date=datetime.datetime(2021, 9, 10)+ datetime.timedelta(days=1))
    obj2.add_child(obj)
    check_US08(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == "" #that means it works as no anomaly messages should pop up


def test_birth_after_marriage(capfd):
    obj = Individual(id = "I01", birth = datetime.datetime(2019, 12, 24) + datetime.timedelta(days=1))
    obj2 = Family(id="F01", marriage_date = datetime.datetime(2019, 11, 17) + datetime.timedelta(days=1))
    obj2.add_child(obj)
    check_US08(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == "" #that means it works as no anomaly messages should pop up

def test2(capfd):
    obj = Individual(id = "I01", birth = datetime.datetime(2008, 12, 1) + datetime.timedelta(days=1))
    obj2 = Family(id="F01", marriage_date = datetime.datetime(2002, 10, 2) + datetime.timedelta(days=1),divorce_date=datetime.datetime(2005, 9, 12)+ datetime.timedelta(days=1))
    obj2.add_child(obj)
    check_US08(obj2)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US08.format(str(obj), obj.birth, obj2.divorce_date)


