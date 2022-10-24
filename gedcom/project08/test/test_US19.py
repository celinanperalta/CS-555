import pytest
import datetime
import consts
from model import Individual, Family
from validator import check_US19
from gedcom import GEDCOM

def test_US19(capfd):
    entries = []
    with open("data/us_19.ged") as file:
        entries = file.readlines()
    gedcom = GEDCOM(entries)
    check_US19(gedcom.families) 
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US19.format("I7", "I8")
