import pandas as pd
import sys
import argparse
import regex
import consts


def is_valid_entry(level, ident, tag, args):
    if tag not in consts.TAGS:
        return f"Error: Unknown tag {tag}"
    if (tag == consts.GEDCOM_TAG_DATE):
        # Very lax check on date format
        re = '(\d{1,2}) ([A-Z]{3}) (\d{4})'
        match = regex.match(re, args)
        if match is None or match.groups()[1] not in consts.MONTHS:
            return f"Error: Bad date {args}"
    
    return "Y"

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
    tag = groups[2]
    args = groups[3][1:]

    valid = "Y" if is_valid_entry(level, ident, tag, args) == "Y" else "N"

    return [level, tag, valid, args, ident] if len(ident) != 0 else [level, tag, valid, args, None]


def main():

    parser = argparse.ArgumentParser(
        description="CS-555 GEDCOM Parser", prog="gedcom.py")
    parser.add_argument("--file", type=argparse.FileType('r'),
                        help="Name of GEDCOM file to read.")
    args = parser.parse_args()

    entries = []
    with args.file as file:
        entries = file.readlines()

    gedcom = pd.DataFrame(columns=["level",  "tag", "valid", "ident", "args"])

    for x in entries:
        row = process_entry(x)
        gedcom.add(row)

        row = list(filter(lambda x: x is not None, row))

        print(f"-> {x.rstrip()}")
        print(f"<-- {'|'.join(row).rstrip()}")
        

    return 0


if __name__ == "__main__":
    main()
