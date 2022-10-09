MONTHS = {
    "JAN": 1, 
    "FEB": 2, 
    "MAR": 3, 
    "APR": 4, 
    "MAY": 5, 
    "JUN": 6, 
    "JUL": 7, 
    "AUG": 8, 
    "SEP": 9, 
    "OCT": 10, 
    "NOV": 11, 
    "DEC": 12
}

GEDCOM_TAG_INDI = "INDI"
GEDCOM_TAG_NAME = "NAME"
GEDCOM_TAG_SEX = "SEX"
GEDCOM_TAG_BIRT = "BIRT"
GEDCOM_TAG_DEAT = "DEAT"
GEDCOM_TAG_FAMC = "FAMC"
GEDCOM_TAG_FAMS = "FAMS"
GEDCOM_TAG_FAM = "FAM"
GEDCOM_TAG_MARR = "MARR"
GEDCOM_TAG_HUSB = "HUSB"
GEDCOM_TAG_WIFE = "WIFE"
GEDCOM_TAG_CHIL = "CHIL"
GEDCOM_TAG_DIV = "DIV"
GEDCOM_TAG_DATE = "DATE"
GEDCOM_TAG_HEAD = "HEAD"
GEDCOM_TAG_TRLR = "TRLR"
GEDCOM_TAG_NOTE = "NOTE"

TAGS = [
    GEDCOM_TAG_INDI,
    GEDCOM_TAG_NAME,
    GEDCOM_TAG_SEX,
    GEDCOM_TAG_BIRT,
    GEDCOM_TAG_DEAT,
    GEDCOM_TAG_FAMC,
    GEDCOM_TAG_FAMS,
    GEDCOM_TAG_FAM,
    GEDCOM_TAG_MARR,
    GEDCOM_TAG_HUSB,
    GEDCOM_TAG_WIFE,
    GEDCOM_TAG_CHIL,
    GEDCOM_TAG_DIV,
    GEDCOM_TAG_DATE,
    GEDCOM_TAG_HEAD,
    GEDCOM_TAG_TRLR,
    GEDCOM_TAG_NOTE
]

# Errors and anomalies go here

MSG_US01 = "Error US01: {0} date {1} is after the current date."
MSG_US02 = "Error US02: {0} marriage date is before birth date."
MSG_US03 = "Error US03: {0} death date is before birth date."
MSG_US07 = "Anomaly US07: {0} is older than 150 years old."
MSG_US04 = "Error US04: {0} and {1}'s marriage date {2} is after divorce date {3}."
MSG_US05 = "Error US05: {0}'s marriage date {1} is after death date {2}."
MSG_US08 = "Anomaly US08: {0} born {1} before marriage on {2}."
MSG_US09 = "Error US09: {0} born {1} after death date on {2}."
MSG_US10 = "Error US05: {0}'s marriage date {1} is less than 14 years after birth date {2}."
MSG_US11 = "Anomaly US11: {0} is in multiple marriages."
MSG_US13 = "Anomaly US13: Siblings {0} and {1} were born less than 8 months apart."
MSG_US15 = "Anomaly US15: Family {0} has more than 15 siblings."
MSG_US17 = "Anomaly US17: {0} is married to descendant/ancestor {1}."





