import datetime

import pandas as pd
from tabulate import tabulate

import consts
import parse as parser
import validator as validator
from model import Family, Individual

class GEDCOM:
    def __init__(self, entries):
        self.entries = entries
        self.df = pd.DataFrame(columns=["level",  "tag", "valid", "args", "ident"])
        self.families = []
        self.individuals = []
        self.anomalies = []
        self.__init_gedcom()

    # Read gedcom entries and print out valid and invalid tags
    # Add entries to a pandas df for easier processing
    def __init_gedcom(self):
        for x in self.entries:
            row = parser.process_entry(x)
            self.df.loc[len(self.df)] = row

            row = list(filter(lambda x: x is not None, row))


        self.__get_individuals()
        self.__get_families()

    def print_valid(self):
        for x in self.entries:
            row = parser.process_entry(x)

            row = list(filter(lambda x: x is not None, row))

            print(f"-> {x.rstrip()}")
            print(f"<-- {'|'.join(row).rstrip()}")


    def print_identifiers(self):
        print(self.df.loc[self.df['ident'].notnull()])

    def print_families(self):
        table = [["ID", "Husband", "Wife", "Children", "Marriage", "Divorce"]]
        for x in self.families:
            table.append(x.to_table_row())
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    
    def print_individuals(self):
        table = [["ID", "Name", "Sex", "Birth", "Death", "FAMC", "FAMS", "AGE"]]
        for individual in self.individuals:
            table.append(individual.to_table_row())
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    def __is_date_entry(self, entry):
        return entry['level'] == '2' and entry['tag'] == consts.GEDCOM_TAG_DATE   

    def __get_individuals(self):
        i = 0
        while i < len(self.df):
            entry = self.df.loc[i]
            if entry['tag'] == consts.GEDCOM_TAG_INDI:
                individual = Individual(id = entry['ident'])
                i += 1
                while (i < len(self.df) and self.df.loc[i]['level'] != 0 and self.df.loc[i]['tag'] != consts.GEDCOM_TAG_INDI):
                    subentry = self.df.loc[i]
                    tag, args = subentry['tag'], subentry['args']
                    if tag == consts.GEDCOM_TAG_NAME:
                        individual.set_name(args)
                    elif tag == consts.GEDCOM_TAG_SEX:
                        individual.set_sex(args)
                    elif tag == consts.GEDCOM_TAG_BIRT:
                        i += 1
                        if (self.__is_date_entry(self.df.loc[i])):
                            individual.set_birth(self.df.loc[i]['args'])
                    elif tag == consts.GEDCOM_TAG_DEAT:
                        i += 1
                        if (self.__is_date_entry(self.df.loc[i])):
                            individual.set_death(self.df.loc[i]['args'])
                    elif tag == consts.GEDCOM_TAG_FAMC:
                        individual.add_famc(args)
                    elif tag == consts.GEDCOM_TAG_FAMS:
                        individual.add_fams(args)
                    i += 1
                self.individuals.append(individual)
            if (i < len(self.df) and self.df.loc[i]['tag'] != consts.GEDCOM_TAG_INDI):
                i += 1
        

    def get_individual(self, id):
        result = list(filter(lambda x: x.id == id, self.individuals))
        return result[0] if len(result) > 0 else None

    def __get_families(self):
        i = 0
        while i < len(self.df):
            entry = self.df.loc[i]
            if entry['tag'] == consts.GEDCOM_TAG_FAM:
                family = Family(id = entry['ident'])
                i += 1
                while i < len(self.df) and self.df.loc[i]['level'] != 0 and self.df.loc[i]['tag'] != consts.GEDCOM_TAG_FAM:
                    subentry = self.df.loc[i]
                    tag, args = subentry['tag'], subentry['args']
                    if tag == consts.GEDCOM_TAG_MARR:
                        family.ln_marriage = i
                        i += 1
                        if (self.__is_date_entry(self.df.loc[i])):
                            family.set_marriage_date(self.df.loc[i]['args'])
                    elif tag == consts.GEDCOM_TAG_HUSB:
                        family.set_husband(self.get_individual(args))
                    elif tag == consts.GEDCOM_TAG_WIFE:
                        family.set_wife(self.get_individual(args))
                    elif tag == consts.GEDCOM_TAG_CHIL:
                        child = self.get_individual(args)
                        if child is not None:
                            family.add_child(child)
                    elif tag == consts.GEDCOM_TAG_DIV:
                        family.ln_divorce = i
                        i += 1
                        if (self.__is_date_entry(self.df.loc[i])):
                            family.set_divorce_date(self.df.iloc[i]['args'])
                    i += 1
                self.families.append(family)
            if (i < len(self.df) and self.df.loc[i]['tag'] != consts.GEDCOM_TAG_FAM):
                i += 1

        


    
