import datetime
from model import Individual, Family
import consts

# TODO: Put all messages into one dict keyed by US##
def get_message(id, item, args):
    pass

def validate(obj):
    if isinstance(obj, Individual):
        check_US01(obj)
        check_US07(obj)
    else:
        check_US01(obj)

def check_US01(obj):
    curr_date = datetime.datetime.now()
    if isinstance(obj, Individual):
        if obj.birth is not None and obj.birth > curr_date:
            print(consts.MSG_US01.format("Birth", obj.birth))
        elif obj.death is not None and obj.death > curr_date:
            print(consts.MSG_US01.format("Death", obj.death))
    elif isinstance(obj, Family):
        if obj.marriage_date is not None and obj.marriage_date > curr_date:
            print(consts.MSG_US01.format("Marriage", obj.marriage_date))
        if obj.divorce_date is not None and obj.divorce_date > curr_date:
            print(consts.MSG_US01.format("Divorce", obj.divorce_date))

# Anomaly US07: Less then 150 years old
def check_US07(individual) -> None:
    curr_date = datetime.datetime.now()
    valid = True

    if individual.birth is None:
        print("Error US##: {0} has no birth date.".format(str(individual))) #TODO: Should this be checked in a different issue?
        return

    if individual.death is None:
        if curr_date - individual.birth > datetime.timedelta(days = 365 * 150):
            valid = False
    else:
        if (individual.death - individual.birth).days >= 365 * 150:
            valid = False
    
    if not valid:
        print(consts.MSG_US07.format(str(individual)))

