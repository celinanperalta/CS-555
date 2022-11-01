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

    check_US35(person1)

    out, err = capfd.reatouterr()
    assert out.strip() == consts.MSG_US35.format("I0")