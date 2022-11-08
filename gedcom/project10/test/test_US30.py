from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US30
from util import gedcom_date_to_datetime
import pprint

def test_US30(): 
    
    h = Individual("I4", "H", "M", birth=gedcom_date_to_datetime("1 JAN 1976"))
    w = Individual("I5", "W", "F", birth=gedcom_date_to_datetime("1 JAN 1977"))

    family = Family("F01", h, w, marriage_date=gedcom_date_to_datetime("1 JAN 1999"), divorce_date=None)

    individuals = [h,w]

    couples = check_US30([family], individuals)
    print(couples)


    assert "I4" in couples.keys()
    assert len(couples.get("I4")) == 1

# def test_divorse():
#     m = Individual("I6", "M", "P", birth=gedcom_date_to_datetime("1 JAN 1976"))
#     p = Individual("I7", "J", "W", birth=gedcom_date_to_datetime("1 JAN 1977"))

#     family2 = Family("F02", m, p, marriage_date=gedcom_date_to_datetime("1 FEB 2000"), divorce_date=gedcom_date_to_datetime("1 FEB 2008"))

#     individuals = [m,p]

#     couples = check_US30([family2], individuals)
#     #print(couples)


#     assert "I6" in couples.keys()
#     assert len(couples.get("I6")) == 0