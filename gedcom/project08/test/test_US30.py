from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US30
from util import gedcom_date_to_datetime
import pprint

def test_US30(): 
    i0 = Individual("I0", "Albert", "M", gedcom_date_to_datetime("1 JAN 2000"))
    i1 = Individual("I1", "Calbert", "M", gedcom_date_to_datetime("1 JAN 2000"))
    i2 = Individual("I2", "Balbert", "M", gedcom_date_to_datetime("1 JAN 2000"))
    i3 = Individual("I3", "Dalbert", "M", gedcom_date_to_datetime("3 JAN 2003"))
    
    children = [i0, i1, i2, i3]

    h = Individual("I4", "H", "M", birth=gedcom_date_to_datetime("1 JAN 1976"))
    w = Individual("I5", "W", "F", birth=gedcom_date_to_datetime("1 JAN 1977"))

    family = Family("F01", h, w, [], marriage_date=gedcom_date_to_datetime("1 JAN 1999"), divorce_date=None)
    family.set_children(children)

    m = Individual("I5", "M", "P", birth=gedcom_date_to_datetime("1 JAN 1976"))
    p = Individual("I6", "J", "W", birth=gedcom_date_to_datetime("1 JAN 1977"))

    family2 = Family("F02", m, p, [], marriage_date=gedcom_date_to_datetime("1 FEB 2000"), divorce_date=None)


    print("livingCouples")

    individuals = [i0, i1, i2, i3, h, w]
    livingCouples = check_US30([family, family2], individuals)


    assert "I4" in livingCouples.keys()
    assert len(livingCouples.get("I4")) == 1