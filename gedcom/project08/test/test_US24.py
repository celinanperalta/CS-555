import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US24
from util import gedcom_date_to_datetime

def test_same_names_and_date(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband1 = Individual("I02", "Jack Doe", "M", datetime.datetime.now())
    wife2 = Individual("I03", "Jane Doe", "F", datetime.datetime.now())
    husband2 = Individual("I04", "Jack Doe", "M", datetime.datetime.now())

    family1 = Family("F01", husband1, wife1, [], gedcom_date_to_datetime("2 AUG 2024"))
    family2 = Family("F02", husband2, wife2, [], gedcom_date_to_datetime("2 AUG 2024"))

    families = [family1, family2]
    individuals = [wife1, husband1, wife2, husband2]

    check_US24(families)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US24.format(wife1.name, husband1.name, family1.marriage_date)

def test_control(capfd):
    wife1 = Individual("I01", "Jane Doe", "F", datetime.datetime.now())
    husband1 = Individual("I02", "Jack Doe", "M", datetime.datetime.now())
    wife2 = Individual("I03", "Jen Doe", "F", datetime.datetime.now())
    husband2 = Individual("I04", "John Doe", "M", datetime.datetime.now())

    family1 = Family("F01", husband1, wife1, [], datetime.datetime.now())
    family2 = Family("F02", husband2, wife2, [], datetime.datetime.now())

    families = [family1, family2]
    individuals = [wife1, husband1, wife2, husband2]

    check_US24(families)

    out, err = capfd.readouterr()
    assert out.strip() == ''