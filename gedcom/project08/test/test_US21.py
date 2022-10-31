import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US21
from util import gedcom_date_to_datetime

def test_wife_m(capfd):
    wife = Individual("I01", "Jane Doe", "M", datetime.datetime.now())
    husband = Individual("I02", "Jack Doe", "M", datetime.datetime.now())

    family = Family("F01", husband, wife, [], datetime.datetime.now())

    families = [family]
    individuals = [wife, husband]

    check_US21(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US21.format(wife,"wife","M")

def test_husband_f(capfd):
    wife = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband = Individual("I02", "Jack Doe", "F", datetime.datetime.now())

    family = Family("F01", husband, wife, [], datetime.datetime.now())

    families = [family]
    individuals = [wife, husband]

    check_US21(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US21.format(husband,"husband","F")

def test_wife_m_husband_f(capfd):
    wife = Individual("I01", "Jane Doe", "M", datetime.datetime.now())
    husband = Individual("I02", "Jack Doe", "F", datetime.datetime.now())

    family = Family("F01", husband, wife, [], datetime.datetime.now())

    families = [family]
    individuals = [wife, husband]

    check_US21(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US21.format(wife,"wife","M") + "\n" + consts.MSG_US21.format(husband,"husband","F")

def test_control(capfd):
    wife = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband = Individual("I02", "Jack Doe", "M", datetime.datetime.now())

    family = Family("F01", husband, wife, [], datetime.datetime.now())

    families = [family]
    individuals = [wife, husband]

    check_US21(family)

    out, err = capfd.readouterr()
    assert out.strip() == ""