import datetime
import consts
from collections import defaultdict, deque
from dateutil import relativedelta


def gedcom_date_to_datetime(d):
    d = d.split(" ", 2)
    return datetime.datetime(int(d[2]), int(consts.MONTHS.get(d[1])), int(d[0]))

def is_date_overlap(d1_start, d1_end, d2_start, d2_end):
    return not (d1_start < d2_end and d1_end > d2_start)

# families: gedcom Family object list
# returns: dictionary of id -> descendants
def get_descendants_map(families):
    descendant_dict = defaultdict(lambda: set())

    for family in families:
        descendant_dict[family.husband.id].update(family.children)
        descendant_dict[family.wife.id].update(family.children)

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

                for itr in descendant_dict[u.id]:
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