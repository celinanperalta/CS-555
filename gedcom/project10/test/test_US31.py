from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US31
from util import gedcom_date_to_datetime
import pprint

def test_US31(): 
    
    h = Individual("I4", "H", "M", birth=gedcom_date_to_datetime("1 JAN 1976"))
    w = Individual("I5", "W", "F", birth=gedcom_date_to_datetime("1 JAN 1977"))

    m = Individual("I6", "M", "P", birth=gedcom_date_to_datetime("1 JAN 1986"))
    p = Individual("I7", "J", "W", birth=gedcom_date_to_datetime("1 JAN 1987"))

    m.add_fams("F02")
    p.add_fams("F02")

    family = Family("F02", m, p, marriage_date=gedcom_date_to_datetime("1 FEB 2000"), divorce_date=gedcom_date_to_datetime("1 FEB 2008"))

    individuals = [h,w, m, p]

    couples = check_US31(individuals)
    #print(couples)


    assert h.id in couples.keys()
    assert len(couples) == 2
