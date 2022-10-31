import pytest
import datetime
import consts
from model import Individual, Family
from src.validator import check_US16
from util import gedcom_date_to_datetime

def test_all_same(capfd):
    i1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    i2 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1951"))
    i3 = Individual("I03", "John Doe", "M", gedcom_date_to_datetime("8 MAY 2000"))
    i4 = Individual("I04", "Jackie Smith", "F", gedcom_date_to_datetime("8 MAY 1970"))
    i5 = Individual("I05", "Jason Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i6 = Individual("I06", "Jaclyn Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))
    i7 = Individual("I07", "Josh Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i8 = Individual("I08", "James Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i9 = Individual("I09", "Josphine Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))

    family1 = Family("F01", i2, i1, [], gedcom_date_to_datetime("10 JUN 2013"))
    family1.set_children([i3, i4, i5])
    family2 = Family("F02", i3, i6, [], gedcom_date_to_datetime("10 JUN 2013"))
    family2.set_children([i7, i8, i9])

    families = [family1,family2]
    individuals = [i1,i2,i3,i4,i5,i6,i7,i8,i9]

    check_US16(family1)
    check_US16(family2)

    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_married_women(capfd):
    i1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    i2 = Individual("I02", "Jack Doe", "F", gedcom_date_to_datetime("8 MAY 1951"))
    i3 = Individual("I03", "John Doe", "F", gedcom_date_to_datetime("8 MAY 2000"))
    i4 = Individual("I04", "Jackie Smith", "F", gedcom_date_to_datetime("8 MAY 1970"))
    i5 = Individual("I05", "Jason Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i6 = Individual("I06", "Jaclyn Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))
    i7 = Individual("I07", "Josh Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i8 = Individual("I08", "James Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i9 = Individual("I09", "Josphine Doe", "F", gedcom_date_to_datetime("8 MAY 1970"))

    family1 = Family("F01", i2, i1, [], gedcom_date_to_datetime("10 JUN 2013"))
    family1.set_children([i3, i4, i5])
    family2 = Family("F02", i3, i6, [], gedcom_date_to_datetime("10 JUN 2013"))
    family2.set_children([i7, i8, i9])

    families = [family1,family2]
    individuals = [i1,i2,i3,i4,i5,i6,i7,i8,i9]

    check_US16(family1)
    check_US16(family2)

    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_married_men_same(capfd):
    i1 = Individual("I01", "Jane Doe", "M", gedcom_date_to_datetime("8 MAY 1919"))
    i2 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1951"))

    family1 = Family("F01", i2, i1, [], gedcom_date_to_datetime("10 JUN 2013"))

    families = [family1]
    individuals = [i1,i2]

    check_US16(family1)

    out, err = capfd.readouterr()
    assert out.strip() == ""

def test_different_son(capfd):
    i1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    i2 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1951"))
    i3 = Individual("I03", "John Smith", "M", gedcom_date_to_datetime("8 MAY 2000"))
    i4 = Individual("I04", "Jackie Smith", "F", gedcom_date_to_datetime("8 MAY 1970"))
    i5 = Individual("I05", "Jason Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i6 = Individual("I06", "Josh Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))

    family1 = Family("F01", i2, i1, [], gedcom_date_to_datetime("10 JUN 2013"))
    family1.set_children([i3, i4, i5, i6])

    families = [family1]
    individuals = [i1,i2,i3,i4,i5,i6]

    check_US16(family1)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US16.format(i2,i3.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i3,i2.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i5,i3.name.split(" ",1)[1])  + "\n" + consts.MSG_US16.format(i6,i3.name.split(" ",1)[1])  

def test_two_different_sons(capfd):
    i1 = Individual("I01", "Jane Doe", "F", gedcom_date_to_datetime("8 MAY 1919"))
    i2 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1951"))
    i3 = Individual("I03", "John Smith", "M", gedcom_date_to_datetime("8 MAY 2000"))
    i4 = Individual("I04", "Jackie Smith", "F", gedcom_date_to_datetime("8 MAY 1970"))
    i5 = Individual("I05", "Jason Doe", "M", gedcom_date_to_datetime("8 MAY 1970"))
    i6 = Individual("I06", "Josh Roberts", "M", gedcom_date_to_datetime("8 MAY 1970"))

    family1 = Family("F01", i2, i1, [], gedcom_date_to_datetime("10 JUN 2013"))
    family1.set_children([i3, i4, i5, i6])

    families = [family1]
    individuals = [i1,i2,i3,i4,i5,i6]

    check_US16(family1)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US16.format(i2,i3.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i2,i6.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i3,i2.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i3,i6.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i5,i3.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i5,i6.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i6,i2.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i6,i3.name.split(" ",1)[1])

def test_married_men_different(capfd):
    i1 = Individual("I01", "Jane Smith", "M", gedcom_date_to_datetime("8 MAY 1919"))
    i2 = Individual("I02", "Jack Doe", "M", gedcom_date_to_datetime("8 MAY 1951"))

    family1 = Family("F01", i2, i1, [], gedcom_date_to_datetime("10 JUN 2013"))

    families = [family1]
    individuals = [i1,i2]

    check_US16(family1)

    out, err = capfd.readouterr()
    assert out.strip() == consts.MSG_US16.format(i1,i2.name.split(" ",1)[1]) + "\n" + consts.MSG_US16.format(i2,i1.name.split(" ",1)[1])

