from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US36
from util import gedcom_date_to_datetime

def test_US36(capfd):
<<<<<<< HEAD
    person1 = Individual("I01","Kristen Smiles", "F", death=gedcom_date_to_datetime("22 NOV 2022"))
=======
    person1 = Individual("I01","Kristen Smiles", "F", death=gedcom_date_to_datetime("12 NOV 2022"))
>>>>>>> 49638562995d2690edbabd24a9ee1b781335c2fa
    person2 = Individual("I02","Jacke Paul", "M", death=gedcom_date_to_datetime("12 OCT 2002"))

    individuals = [person1, person2]

    check_US36(individuals)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US36.format(person1.name)

 