import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US10
from util import gedcom_date_to_datetime

def test_marriage_wife_minor(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 2000"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1996"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))

    families = [family]
    individuals = [wife, husband]

    check_US10(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US10.format(wife,"2013","2000")

def test_marriage_husband_minor(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1996"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))

    families = [family]
    individuals = [wife, husband]

    check_US10(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US10.format(husband,"2013","2000")

def test_marriage_both_minor(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 2000"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))

    families = [family]
    individuals = [wife, husband]

    check_US10(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US10.format(wife,"2013","2000") + "\n" + consts.MSG_US10.format(husband,"2013","2000")

def test_marriage_both_adult(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1996"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1996"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))

    families = [family]
    individuals = [wife, husband]

    check_US10(family)

    out, err = capfd.readouterr()
    assert out.strip() == ""