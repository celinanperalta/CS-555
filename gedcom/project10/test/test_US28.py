from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US28
from util import gedcom_date_to_datetime
import pprint

def test_US28(capfd):
    children = []

    children.append(Individual("I0", "Serena", "F", gedcom_date_to_datetime("6 MAR 2001")))
    children.append(Individual("I1", "Sophia", "F", gedcom_date_to_datetime("20 APR 2005")))

    family = Family("F01", None, None, [], None, None)
    family.set_children(children)
    check_US28(family)


    out, err = capfd.readouterr()
    assert check_US28(family)

