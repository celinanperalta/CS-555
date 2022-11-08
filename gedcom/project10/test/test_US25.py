import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US25
from util import gedcom_date_to_datetime


def test_US25(capfd):

    children = []
    
    children.append(Individual("I0", "Albert", "M", gedcom_date_to_datetime("1 JAN 2000")))
    children.append(Individual("I1", "Albert", "M", gedcom_date_to_datetime("1 JAN 2000")))
    children.append(Individual("I2", "Balbert", "M", gedcom_date_to_datetime("1 JAN 2000")))
    children.append(Individual("I3", "Balbert", "M", gedcom_date_to_datetime("3 JAN 2003")))

    family = Family("F01", None, None, [], None, None)
    family.set_children(children)
    check_US25(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US25.format("I1", family.id)
