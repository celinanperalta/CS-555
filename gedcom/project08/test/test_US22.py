import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US22
from util import gedcom_date_to_datetime

def test_same_i_id(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband1 = Individual("I02", "Jack Doe", "M", datetime.datetime.now())
    wife2 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband2 = Individual("I03", "Jack Doe", "M", datetime.datetime.now())

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())
    family2 = Family("F02", husband2, wife2, [], datetime.datetime.now())

    families = [family1, family2]
    individuals = [wife1, husband1, wife2, husband2]

    check_US22(individuals, families)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US22.format(wife1.id,"individual")

def test_same_f_id(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband1 = Individual("I02", "Jack Doe", "M", datetime.datetime.now())
    wife2 = Individual("I03", "Jane Doe", "F", datetime.datetime.now())
    husband2 = Individual("I04", "Jack Doe", "M", datetime.datetime.now())

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())
    family2 = Family("F01", husband2, wife2, [], datetime.datetime.now())

    families = [family1, family2]
    individuals = [wife1, husband1, wife2, husband2]

    check_US22(individuals, families)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US22.format(family1.id,"family")

def test_same_f_and_i_id(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband1 = Individual("I02", "Jack Doe", "M", datetime.datetime.now())
    wife2 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband2 = Individual("I04", "Jack Doe", "M", datetime.datetime.now())

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())
    family2 = Family("F01", husband2, wife2, [], datetime.datetime.now())

    families = [family1, family2]
    individuals = [wife1, husband1, wife2, husband2]

    check_US22(individuals, families)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US22.format(wife1.id,"individual") + '\n' + consts.MSG_US22.format(family1.id,"family")

def test_control(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband1 = Individual("I02", "Jack Doe", "M", datetime.datetime.now())
    wife2 = Individual("I03", "Jane Doe", "F", datetime.datetime.now())
    husband2 = Individual("I04", "Jack Doe", "M", datetime.datetime.now())

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())
    family2 = Family("F02", husband2, wife2, [], datetime.datetime.now())

    families = [family1, family2]
    individuals = [wife1, husband1, wife2, husband2]

    check_US22(individuals, families)

    out, err = capfd.readouterr()
    assert out.strip() == ''