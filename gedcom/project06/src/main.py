#!/usr/bin/env python
import argparse
import sys

import pandas as pd
import regex

import consts
import parse as parser
from gedcom import GEDCOM
from validator import check_US17


def main():
    parser = argparse.ArgumentParser(
        description="CS-555 GEDCOM Parser", prog="main.py")
    parser.add_argument("--file", type=argparse.FileType('r'),
                        help="Name of GEDCOM file to read.")
    args = parser.parse_args()

    entries = []
    with args.file as file:
        entries = file.readlines()

    gedcom = GEDCOM(entries)
    
    gedcom.print_individuals()
    gedcom.print_families()

    gedcom.validate_entities()

    return 0


if __name__ == "__main__":
    main()
