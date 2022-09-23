import datetime
import gedcom

# TODO: Put all messages into one dict keyed by US##
def get_message(id, item, args):
    pass

def validate(object):
    if isinstance(object, gedcom.Individual):
        check_US07(object)
    else:
        pass



# Anomaly US07: Less then 150 years old
def check_US07(individual) -> None:
    curr_date = datetime.datetime.now()
    valid = True
    if individual.birth is None:
        print(f"Error US##: {str(individual)} has no birth date.") #TODO: This should be checked in a different ticket?
        return

    if individual.death is None:
        if curr_date - individual.birth > datetime.timedelta(days = 365 * 150):
            valid = False
    else:
        if (individual.death - individual.birth).days >= 365 * 150:
            valid = False
    
    if not valid:
        print(f"Anomaly US07: {str(individual)} is more than 150 years old.")

