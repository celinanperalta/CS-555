from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US35
from util import gedcom_date_to_datetime
import pprint

def test_US35(capfd):
    person1 = Individual("I01", "Kristen Smiles", "F", birth=gedcom_date_to_datetime("12 OCT 2022"))
    person2 = Individual("I02", "Chris Smiles", "F", birth=gedcom_date_to_datetime("1 JAN 2001"))

    individuals = [person1, person2]
    check_US35(individuals)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US35.format()