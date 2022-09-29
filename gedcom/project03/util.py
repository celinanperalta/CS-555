import datetime
import consts

def gedcom_date_to_datetime(d):
    d = d.split(" ", 2)
    return datetime.datetime(int(d[2]), int(consts.MONTHS.get(d[1])), int(d[0]))