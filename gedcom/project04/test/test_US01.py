import pytest
import datetime
import sys
from src import consts
from src.model import Individual, Family
from src.validator import check_US01

def test_invalid_birth(capfd):
    obj = Individual(id="I01", birth = datetime.datetime.now() + datetime.timedelta(days=1))
    check_US01(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US01.format("Birth", obj.birth)

def test_invalid_death(capfd):
    obj = Individual(id="I01", death = datetime.datetime.now() + datetime.timedelta(days=1))
    check_US01(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US01.format("Death", obj.death)

def test_invalid_marriage(capfd):
    obj = Family(id="F01", marriage_date=datetime.datetime.now() + datetime.timedelta(days=1))
    check_US01(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US01.format("Marriage", obj.marriage_date)

def test_invalid_divorce(capfd):
    obj = Family(id="F01", divorce_date=datetime.datetime.now() + datetime.timedelta(days=1))
    check_US01(obj)
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US01.format("Divorce", obj.divorce_date)

def test_empty(capfd):
    obj = Individual(id="I01")
    check_US01(obj)
    out, err = capfd.readouterr()
    assert out == ""
