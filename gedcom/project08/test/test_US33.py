from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US33
from util import gedcom_date_to_datetime
import pprint

def test_US33():

    i0 = Individual("I0", "Bob", "M", gedcom_date_to_datetime("1 JAN 2000"))
    i1 = Individual("I1", "Jim", "M", gedcom_date_to_datetime("1 JAN 2000"))
    i2 = Individual("I2", "Sue", "M", gedcom_date_to_datetime("1 JAN 2000"))
    i3 = Individual("I3", "Karen", "M", gedcom_date_to_datetime("3 JAN 2003"))
    
    children = [i0, i1, i2, i3]

    h = Individual("I4", "H", "M", birth=gedcom_date_to_datetime("1 JAN 1976"), death=datetime.datetime.now())
    w = Individual("I5", "W", "F", birth=gedcom_date_to_datetime("1 JAN 1977"))

    family = Family("F01", h, w, [], marriage_date=gedcom_date_to_datetime("1 JAN 1999"), divorce_date=None)
    family.set_children(children)

    individuals = [i0, i1, i2, i3, h, w]
    survivors = check_US37([family], individuals)

    assert "I4" in survivors.keys()
    assert len(survivors.get("I4")) == 4