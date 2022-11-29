from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US32
from util import gedcom_date_to_datetime
import pprint

def test_US32(): 
    
    h = Individual("I4", "H", "M", birth=gedcom_date_to_datetime("1 JAN 1977"))
    w = Individual("I5", "W", "F", birth=gedcom_date_to_datetime("1 JAN 1977"))

    m = Individual("I6", "M", "P", birth=gedcom_date_to_datetime("1 JAN 1977"), fams = "F02")
    p = Individual("I7", "J", "W", birth=gedcom_date_to_datetime("1 JAN 1977"), fams = "F02")

    individuals = [h,w, m, p]

    births = check_US32(individuals)
    #print(couples)

    assert len(births) == 4