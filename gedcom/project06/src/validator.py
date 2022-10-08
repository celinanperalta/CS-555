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
        check_US04(obj)
        check_US05(obj)
        check_US10(obj)
        check_US12(obj)
        check_US16(obj)

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

# Error US02: Birth before marriage
def check_US02(family, individual):
    if (individual.birth is not None and family.marriage_date is not None):
        if(individual.birth < family.marriage_date):
            print(consts.MSG_US02.format(str(individual), individual.birth, family.marriage_date))
        if (individual.birth == family.marriage_date):
            print(consts.MSG_US02.format(str(individual), individual.birth, family.marriage_date))
    if (individual.birth is None or family.marriage_date is None):
        print("Error: no input")


# Error US03: Birth before death
def check_US03(individual) -> None:
    if individual.birth is not None and individual.death is not None and individual.birth < individual.death:
        print(consts.MSG_US03.format(str(individual.birth), individual.death))
    if individual.birth == individual.death:
        print(consts.MSG_US03.format(str(individual.birth), individual.death))

# Error US04: Marriage before divorce
def check_US04(family) -> None:
    if family.divorce_date is not None and (family.marriage_date is None or family.marriage_date > family.divorce_date):
        print(consts.MSG_US04.format(str(family.wife), str(family.husband), family.marriage_date, family.divorce_date))

# Error US05: Marriage before death
def check_US05(family) -> None:
    if family.wife.death is not None and family.marriage_date is not None and family.wife.death < family.marriage_date:
        print(consts.MSG_US05.format(str(family.wife), family.marriage_date, family.wife.death))
    if family.husband.death is not None and family.marriage_date is not None and family.husband.death < family.marriage_date:
        print(consts.MSG_US05.format(str(family.husband), family.marriage_date, family.husband.death))
    
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

#birth before marriage/divource of parents
def check_US08(family, individual):
    if(family.divorce_date is not None and family.marriage_date is not None):
        if(individual.birth < family.marriage_date):
            print(consts.MSG_US08.format(str(individual), individual.birth, family.marriage_date)) 

        #average days in a month is 30.4
        if((((individual.birth - (family.divorce_date)).days))/30.4 > 9):
            print(consts.MSG_US08.format(str(individual), individual.birth, family.divorce_date))

    if(family.marriage_date is not None and family.divorce_date is None):
        if(individual.birth < family.marriage_date):
            print(consts.MSG_US08.format(str(individual), individual.birth, family.marriage_date)) 
    

#birth before death of parents
def check_US09(family, individual):
    if(family.wife.death is not None):
        if(individual.birth < family.wife.death):
            print(consts.MSG_US09.format(str(individual), individual.birth, family.wife.death))
    elif(family.husband.death is not None):
        if((((individual.birth - (family.husband.death)).days))/30.4 > 9):
            print(consts.MSG_US09.format(str(individual), individual.birth, family.husband.death))

#marriage after 14 for both spouses
def check_US10(family) -> None:    
    if family.wife.birth is not None and family.marriage_date is not None and family.wife.birth.year + 14 > family.marriage_date.year:
        print(consts.MSG_US10.format(str(family.wife), family.marriage_date.year, family.wife.birth.year))
    if family.husband.birth is not None and family.marriage_date is not None and family.husband.birth.year + 14 > family.marriage_date.year:
        print(consts.MSG_US10.format(str(family.husband), family.marriage_date.year, family.husband.birth.year))

#Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
def check_US12(family) -> None:
    if family.children is not None and len(family.children) > 0:
        for child in family.children:
            if family.wife.birth is not None and child.birth is not None and family.wife.birth.year + 60 < child.birth.year:
                print(consts.MSG_US12.format(str(family.wife), family.wife.birth.year, 60, str(child), child.birth.year))
            if family.husband.birth is not None and child.birth is not None and family.husband.birth.year + 80 < child.birth.year:
                print(consts.MSG_US12.format(str(family.husband), family.husband.birth.year, 80, str(child), child.birth.year))

#All male members of a family should have the same last name
def check_US16(family) -> None:
    if family.children is not None and len(family.children) > 0:
        sons = []
        for child in family.children:
            if  child.name is not None and child.sex == "M" and family.husband is not None and family.husband.name is not None and family.husband.sex == "M" and family.husband.name.split(" ",1)[1] != child.name.split(" ",1)[1]:
                print(consts.MSG_US16.format(str(child), family.husband.name.split(" ",1)[1], child.sex))
            if child.name is not None and child.sex == "M" and child.name.split(" ",1)[1] not in sons:
                sons += [child.name.split(" ",1)[1]]
                for name in sons:
                    if name != child.name.split(" ",1)[1]:
                        print(consts.MSG_US16.format(str(child), name, child.sex))