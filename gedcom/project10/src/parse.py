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