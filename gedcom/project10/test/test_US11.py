import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US11
from util import gedcom_date_to_datetime

def test_marriage_no_divorce(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1996"))
    husband1 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1996"))
    husband2 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 1996"))

    family1 = Family("F01", husband1, wife, [], gedcom_date_to_datetime("10 JUN 2020"))
    family2 = Family("F02", husband2, wife, [], gedcom_date_to_datetime("10 JUL 2020"))

    families = [family1, family2]
    individuals = [wife, husband1, husband2]

    check_US11(families)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US11.format(wife.id)


def test_marriage_with_divorce(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1996"))
    husband1 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1996"))
    husband2 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 1996"))

    family1 = Family("F01", husband1, wife, [], gedcom_date_to_datetime("10 JUN 2020"), gedcom_date_to_datetime("19 JUN 2020"))
    family2 = Family("F02", husband2, wife, [], gedcom_date_to_datetime("10 JUL 2020"))

    families = [family1, family2]
    individuals = [wife, husband1, husband2]

    check_US11(families)

    out, err = capfd.readouterr()
    assert out.strip() == ""