import datetime
import consts
from collections import defaultdict, deque
from dateutil import relativedelta


def gedcom_date_to_datetime(d):
    d = d.split(" ")

    if len(d) == 3:
        return datetime.datetime(int(d[2]), int(consts.MONTHS.get(d[1])), int(d[0]))
    elif len(d) == 2:
        return datetime.datetime(int(d[1]), int(consts.MONTHS.get(d[0])), 1)
    else:
        return datetime.datetime(int(d[0]), 1, 1)

def is_date_overlap(d1_start, d1_end, d2_start, d2_end):
    return not (d1_start < d2_end and d1_end > d2_start)

# families: gedcom Family object list
# returns: dictionary of id -> descendants
def get_descendants_map(families):
    descendant_dict = defaultdict(lambda: set())

    for family in families:
        if family.husband is None or family.wife is None:
            continue
        descendant_dict[family.husband].update(family.children)
        descendant_dict[family.wife].update(family.children)

    new_dict = defaultdict(lambda: set())

    for k in descendant_dict.copy():
        children = descendant_dict[k]
        for item in children:
            seen = {item.id}
            dq = deque()
            reachable = []
            dq.append(item)
            while (len(dq) > 0):
                u = dq.popleft()
                reachable.append(u)

                for itr in descendant_dict[u]:
                    if itr.id not in seen:
                        seen.add(itr.id)
                        dq.append(itr)

            new_dict[k].update(descendant_dict[k])
            new_dict[k].update(reachable)
    
    return new_dict


def get_relativedelta(d1, d2):
    delta: relativedelta.relativedelta = relativedelta.relativedelta(d1, d2)
    days = abs((d1 - d2).days)
    months = abs(delta.years * 12 + delta.months)

    return days, months

def get_children_of_individuals(families):
    marriages = []
    children_map = defaultdict(lambda: [])
    for family in families:
        if (family.marriage_date is not None):
            marriages += [(family.husband.id, family.wife.id)]
        children_map[family.husband.id] += family.children
        children_map[family.wife.id] += family.children

def get_age_in_years(i):
    return abs(relativedelta.relativedelta(i.birth, datetime.datetime.now()).years)

def get_marriage_length_in_years(f):
    return abs(relativedelta.relativedelta(f.marriage_date, datetime.datetime.now()).years)