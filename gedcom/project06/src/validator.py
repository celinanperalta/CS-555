import datetime
import pprint
from collections import defaultdict, deque
from functools import reduce
from itertools import combinations, permutations, product
from typing import List

from dateutil import relativedelta

import consts
from model import Family, Individual
from util import get_descendants_map, is_date_overlap, get_relativedelta



# TODO: Put all messages into one dict keyed by US##
def get_message(id, item, args):
    pass

def validate(gedcom):
    for x in gedcom.individuals:
        validate_obj(x)
    for x in gedcom.families:
        validate_obj(x)

    # Checks that require entire list of families
    check_US11(gedcom.families)
    check_US17(gedcom.families)
    check_US19(gedcom.families)
    check_US20(gedcom.families)
    
# For validations that take singleton objects (i.e. Family, Individual)
def validate_obj(obj):
    if isinstance(obj, Individual):
        check_US01(obj)
        check_US07(obj)
    else:
        check_US01(obj)
        check_US04(obj)
        check_US05(obj)
        check_US14(obj)
        check_US18(obj)
        check_US15(obj)
        check_US10(obj)
        check_US12(obj)
     #   check_US16(obj)
        check_US13(obj)


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

#First cousins should not marry one another
def check_US19(families):
#   find all families where marriage date != null
#   Find sibling sets, see if they have kids, then see if kids are married
    marriages = []
    children_map = defaultdict(lambda: [])
    for family in families:
        if (family.marriage_date is not None):
            marriages += [(family.husband.id, family.wife.id)]
        children_map[family.husband.id] += family.children
        children_map[family.wife.id] += family.children

    for family in families:
        siblings = family.children
        siblings_children = []
        for x in siblings:
            siblings_children += children_map[x.id]
        pairs = list(combinations(siblings_children,2))
        all_pairs = []
        for x in pairs: 
            all_pairs += [(x[0].id, x[1].id)]
            all_pairs += [(x[1].id, x[0].id)]
        for x in all_pairs:
            if (x in marriages):
                print(consts.MSG_US19.format(x[0], x[1]))
                
  

#no more than 5 births
def check_US14(family):
    sibling = family.children
    siblingBirthday = {}

    for i in sibling:
        if(i.birth not in siblingBirthday):
            siblingBirthday[i.birth] = 1 
            #print(family.id)
            #print(siblingBirthday)
        else:
            siblingBirthday[i.birth] += 1
            #print(family.id)
            #print(siblingBirthday)
        if(siblingBirthday[i.birth] > 5):
            print(consts.MSG_US14.format((family.id)))

#siblings cannot marry each other
def check_US18(family) -> None:
    sibling = family.children
    siblingMarriage = {}

    for i in sibling:
        if(i.fams is not None):
            if(i.fams not in siblingMarriage):
                siblingMarriage[i.fams] = 1 
                #print(i)
                #print(siblingMarriage)
            else:
                siblingMarriage[i.fams] += 1
                #print(i)
                #print(siblingMarriage)
            if(siblingMarriage[i.fams] > 1):
                print(consts.MSG_US18.format(str(i.id)))


def US11_get_marriage_dict(families):
    marriage_dict = defaultdict(lambda: [])

    for family in families:
        if family.marriage_date is not None:
            marriage_details =  [[family.marriage_date, family.divorce_date if family.divorce_date is not None else datetime.datetime(4000, 1, 1, 1, 1)]]
            marriage_dict[family.husband.id] += marriage_details
            marriage_dict[family.wife.id] += marriage_details
    
    return marriage_dict
    
# Marriage should not occur during marriage to another spouse
def check_US11(families):
    marriage_dict = US11_get_marriage_dict(families)

    for k,v in marriage_dict.items():
        dates = sorted(v, key=lambda x: x[0])
        valid = reduce(lambda x,y: is_date_overlap(x[0], x[1], y[0], y[1]), dates)
    
        if not valid:
            print(consts.MSG_US11.format(k))

#Birth dates of siblings should be more than 8 months apart or less than 
# 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
def check_US13(family):
    sibling_pairs = list(combinations(family.children, 2))
    for pair in sibling_pairs:
        if (pair[0].birth is not None and pair[1].birth is not None):
            days_between, months_between = get_relativedelta(pair[0].birth, pair[1].birth)
            if not (days_between < 2 or months_between >= 8):
                print(consts.MSG_US13.format(pair[0].id, pair[1].id))
    

# There should be fewer than 15 siblings in a family
def check_US15(family):
    if len(family.children) >= 15:
        print(consts.MSG_US15.format(family.id))

# Parents should not marry any of their descendants
def check_US17(families: List[Family]):
    descendants = get_descendants_map(families)

    for family in families:
        husband_descendants = list(map(lambda x: x.id, descendants[family.husband.id]))
        wife_descendants = list(map(lambda x: x.id, descendants[family.wife.id]))
        if family.husband.id in wife_descendants or family.wife.id in husband_descendants:
            print(consts.MSG_US17.format(family.husband.id, family.wife.id))

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
    members = []
    if (family.wife is not None):
        members.append(family.wife)
    if (family.husband is not None):
        members.append(family.husband)
    if family.children is not None and len(family.children) > 0:
        members.extend(family.children)
    men = []
    last_names = []
    hasPrinted = False
    for member in members:
        if member.name is not None and member.sex == "M":
            if (member.name.split(" ",1)[1] not in last_names):
                last_names.append(member.name.split(" ",1)[1])
            men.append(member)
    
    for member in men:
        for last_name in last_names:
            if last_name != member.name.split(" ",1)[1]:
                print(consts.MSG_US16.format((member.name + " (" + member.id + ")"), last_name))

#Aunts and uncles should not marry their nieces or nephews
def check_US20(families):
    #Check if niece or nephew's parents are aunt or uncles siblings

    marriages = []
    children_map = defaultdict(lambda: [])
    for family in families:
        if (family.marriage_date is not None):
            marriages += [(family.husband.id, family.wife.id)]
        children_map[family.husband.id] += [x.id for x in family.children]
        children_map[family.wife.id] += [x.id for x in family.children]
  
    for family in families:
        au = [x.id for x in family.children]
        nn = []
        for sibling in au:
            for other_sibling in au:
                if (sibling != other_sibling):
                    nn += children_map[other_sibling]
                    
        check_marriages = product(au, nn)
        for c in check_marriages:
            if (c[0], c[1]) in marriages:
                print(consts.MSG_US20.format(c[0], c[1]))
            if (c[1], c[0]) in marriages:
                print(consts.MSG_US20.format(c[1], c[0]))
