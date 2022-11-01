from pprint import pprint
import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US35
from util import gedcom_date_to_datetime
import pprint

def test_US35(capfd):
    
