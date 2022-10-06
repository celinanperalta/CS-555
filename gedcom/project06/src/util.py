import datetime
import consts

def gedcom_date_to_datetime(d):
    d = d.split(" ", 2)
    return datetime.datetime(int(d[2]), int(consts.MONTHS.get(d[1])), int(d[0]))

def is_date_overlap(d1_start, d1_end, d2_start, d2_end):
    return not (d1_start < d2_end and d1_end > d2_start)

