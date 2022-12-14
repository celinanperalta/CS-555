import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US23
from util import gedcom_date_to_datetime

def test_same_name_and_birth(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("2 AUG 2022"))
    husband1 = Individual("I02", "Jane Doe", "M", gedcom_date_to_datetime("2 AUG 2022"))

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())

    families = [family1]
    individuals = [wife1, husband1]

    check_US23(individuals)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US23.format(wife1.name,wife1.birth)

def test_same_name(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("3 AUG 2022"))
    husband1 = Individual("I02", "Jane Doe", "M", gedcom_date_to_datetime("2 AUG 2022"))

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())

    families = [family1]
    individuals = [wife1, husband1]

    check_US23(individuals)

    out, err = capfd.readouterr()
    assert out.strip() == ''

def test_same_birth(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("2 AUG 2022"))
    husband1 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("2 AUG 2022"))

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())

    families = [family1]
    individuals = [wife1, husband1]

    check_US23(individuals)

    out, err = capfd.readouterr()
    assert out.strip() == ''

def test_control(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("2 AUG 2022"))
    husband1 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("3 AUG 2022"))

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())

    families = [family1]
    individuals = [wife1, husband1]

    check_US23(individuals)

    out, err = capfd.readouterr()
    assert out.strip() == ''