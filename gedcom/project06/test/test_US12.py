import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US12
from util import gedcom_date_to_datetime

def test_old_wife_one_kid(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1951"))
    child1 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    child2 = Individual("I04", "Jackie Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))
    family.set_children([child1, child2])

    families = [family]
    individuals = [wife, husband, child1, child2]

    check_US12(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US12.format(wife,"1919","60",child1,"2000")

def test_old_husband_one_kid(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1961"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1919"))
    child1 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    child2 = Individual("I04", "Jackie Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))
    family.set_children([child1, child2])

    families = [family]
    individuals = [wife, husband,child1,child2]

    check_US12(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US12.format(husband,"1919","80",child1,"2000")

def test_old_both_one_kid(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1919"))
    child1 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    child2 = Individual("I04", "Jackie Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))
    family.set_children([child1, child2])

    families = [family]
    individuals = [wife, husband,child1,child2]

    check_US12(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US12.format(wife,"1919","60",child1,"2000") + "\n" + consts.MSG_US12.format(husband,"1919","80",child1,"2000")

def test_old_wife_both_kids(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1961"))
    child1 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    child2 = Individual("I04", "Jackie Doe", "F", gedcom_date_to_datetime("8 MAY 2002"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))
    family.set_children([child1, child2])

    families = [family]
    individuals = [wife, husband,child1,child2]

    check_US12(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US12.format(wife,"1919","60",child1,"2000") + "\n" + consts.MSG_US12.format(wife,"1919","60",child2,"2002")

def test_old_husband_both_kids(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1961"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1919"))
    child1 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    child2 = Individual("I04", "Jackie Doe", "F", gedcom_date_to_datetime("8 MAY 2002"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))
    family.set_children([child1, child2])

    families = [family]
    individuals = [wife, husband,child1,child2]

    check_US12(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US12.format(husband,"1919","80",child1,"2000") + "\n" + consts.MSG_US12.format(husband,"1919","80",child2,"2002")

def test_old_both_both_kids(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1919"))
    child1 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    child2 = Individual("I04", "Jackie Doe", "F", gedcom_date_to_datetime("8 MAY 2002"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))
    family.set_children([child1, child2])

    families = [family]
    individuals = [wife, husband,child1,child2]

    check_US12(family)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US12.format(wife,"1919","60",child1,"2000") + "\n" + consts.MSG_US12.format(husband,"1919","80",child1,"2000") + "\n" + consts.MSG_US12.format(wife,"1919","60",child2,"2002") + "\n" + consts.MSG_US12.format(husband,"1919","80",child2,"2002")

def test_old_none(capfd):
    wife = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))
    husband = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    child1 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    child2 = Individual("I04", "Jackie Doe", "F", gedcom_date_to_datetime("8 MAY 2002"))

    family = Family("F01", husband, wife, [], gedcom_date_to_datetime("10 JUN 2013"))
    family.set_children([child1, child2])

    families = [family]
    individuals = [wife, husband,child1,child2]

    check_US12(family)

    out, err = capfd.readouterr()
    assert out.strip() == ""