from typing import List

import regex

import consts


def is_valid_tag(tag):
    return tag in consts.TAGS

# US41 Accept and use dates without days or without days and months
def is_valid_date(date):
    # Very lax check on date format
    re = '(\d{1,2}) ([A-Z]{3}) (\d{4})'
    match = regex.match(re, date)
    if match and match.groups()[1] in consts.MONTHS.keys():
        return True
    
    re = '([A-Z]{3}) (\d{4})'
    match = regex.match(re, date)
    if match and match.groups()[0] in consts.MONTHS.keys():
        return True

    re = '(\d{4})'
    match = regex.match(re, date)
    if match:
        return True

    return False

# US42 All dates should be legitimate dates for the months specified (e.g., 2/30/2015 is not legitimate)
def reject_invalid_date(date):
    re = '(\d{1,2}) ([A-Z]{3}) (\d{4})'
    match = regex.match(re, date)
    if match.groups()[0] == '1' or match.groups()[0] == '3' or match.groups()[0] == '5' or match.groups()[0] == '7' or match.groups()[0] == '8' or match.groups()[0] == '10' or match.groups()[0] == '12':
        if match.groups()[1] > 31:
            return True

    if match.groups()[0] == '4' or match.groups()[0] == '6' or match.groups()[0] == '9' or match.groups()[0] == '11':
        if match.groups()[1] > 30:
            return True

    if match.groups()[0] == '2':
        if match.groups()[2] % 4 == 0:
            if match.groups()[1] > 29:
                return True
        else:
            if match.groups()[1] > 28:
                return True
    
    return False

    
# Input: [level, tag, args, ident] from GEDCOM file
# Output: True if valid
def is_valid_entry(level, ident, tag, args):
    if not is_valid_tag(tag):
        return False

    if (tag == consts.GEDCOM_TAG_DATE):
        if not is_valid_date(args):
            return False
        
    return True

# Input: A line of a GEDCOM file
# Output: [level, tag, valid, args, ident]
def process_entry(entry):

    level_re = '^(0|[1-9]+\d*) '
    ident_re = '(@[^@]+@ |)'
    tag_re = '([A-Za-z0-9_]+)'
    args_re = '( [^\n\r]*|)'

    gedcom_regex = level_re + ident_re + tag_re + args_re

    match = regex.match(gedcom_regex, entry)

    groups = match.groups()
    level = groups[0]
    ident = groups[1].rstrip(' ')
    ident = ident.replace("@", "")
    tag = groups[2]
    args = groups[3][1:]
    args = args.replace("@", "")

    valid = "Y" if is_valid_entry(level, ident, tag, args) else "N"

    # If there is no identifier (@I1@, @F6@, etc.), return None for the identifier.
    return [level, tag, valid, args, ident] if len(ident) != 0 else [level, tag, valid, args, None]