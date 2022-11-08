import pytest
import datetime
import consts
from model import Individual, Family
from validator import check_US20
from gedcom import GEDCOM

def test_US20(capfd):
    entries = []
    with open("data/us_20.ged") as file:
        entries = file.readlines()
    gedcom = GEDCOM(entries)
    check_US20(gedcom.families) 
    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US20.format("I9", "I1")
