from tabulate import tabulate
import pandas as pd
import parser as parser
import consts

class Individual:

    def __init__(self, id, name = None, sex = None, birth = None, death = None, famc = None, fams = None) -> None:
        self.id = id
        self.name = name
        self.sex = sex
        self.birth = birth
        self.death = death
        self.famc = famc
        self.fams = fams

    def set_name(self, name):
        self.name = name

    def set_sex(self, sex):
        self.sex = sex
    
    def set_birth(self, birth):
        self.birth = birth
    
    def set_death(self, death):
        self.death = death
    
    def set_famc(self, famc):
        self.famc = famc

    def set_fams(self, fams):
        self.fams = fams

    def __str__(self):
        return f"{self.id} {self.name}"


class Family:
    def __init__(self, id, husband = None, wife = None, children = [], marriage_date = None, divorce_date = None) -> None:
        self.id = id
        self.husband = husband
        self.wife = wife
        self.children = []
        self.marriage_date = marriage_date
        self.divorce_date = divorce_date

    def set_id(self, id):
        self.id = id
    
    def set_husband(self, husband):
        self.husband = husband
    
    def set_wife(self, wife):
        self.wife = wife
    
    def set_children(self, children):
        self.children.clear()
        for x in children:
            self.children.append(x)

    def set_marriage_date(self, marriage_date):
        self.marriage_date = marriage_date

    def set_divorce_date(self, divorce_date):
        self.divorce_date = divorce_date

    def add_child(self, child):
        self.children.append(child)

    # For pretty printing families
    def to_table_row(self):
        return [self.id, self.husband.name, self.wife.name, [x.id for x in self.children], self.marriage_date, self.divorce_date]
    
    def __str__(self):
        return f"{self.id} {self.husband.name} {self.wife.name}"

class GEDCOM:
    def __init__(self, entries):
        self.entries = entries
        self.df = pd.DataFrame(columns=["level",  "tag", "valid", "args", "ident"])
        self.families = []
        self.individuals = []
        self.__init_gedcom()

    # Read gedcom entries and print out valid and invalid tags
    # Add entries to a pandas df for easier processing
    def __init_gedcom(self):
        for x in self.entries:
            row = parser.process_entry(x)
            self.df.loc[len(self.df)] = row

            row = list(filter(lambda x: x is not None, row))

            print(f"-> {x.rstrip()}")
            print(f"<-- {'|'.join(row).rstrip()}")

        self.__get_individuals()
        self.__get_families()

    def print_identifiers(self):
        print(self.df.loc[self.df['ident'].notnull()])

    def print_families(self):
        table = [["ID", "Husband", "Wife", "Children", "Marriage", "Divorce"]]
        for x in self.families:
            table.append(x.to_table_row())
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    
    def print_individuals(self):
        table = [["ID", "Name", "Sex", "Birth", "Death", "FAMC", "FAMS"]]
        for x in self.individuals:
            rows = x.__dict__.values()
            table.append(x.__dict__.values())
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
                        individual.set_famc(args)
                    elif tag == consts.GEDCOM_TAG_FAMS:
                        individual.set_fams(args)
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
                        i += 1
                        if (self.__is_date_entry(self.df.loc[i])):
                            family.marriage_date = self.df.loc[i]['args']
                    elif tag == consts.GEDCOM_TAG_HUSB:
                        family.set_husband(self.get_individual(args))
                    elif tag == consts.GEDCOM_TAG_WIFE:
                        family.set_wife(self.get_individual(args))
                    elif tag == consts.GEDCOM_TAG_CHIL:
                        child = self.get_individual(args)
                        if child is not None:
                            family.add_child(child)
                    elif tag == consts.GEDCOM_TAG_DIV:
                        i += 1
                        if (self.__is_date_entry(self.df.loc[i])):
                            family.set_divorce_date(self.df.iloc[i]['args'])
                    i += 1
                self.families.append(family)
            if (i < len(self.df) and self.df.loc[i]['tag'] != consts.GEDCOM_TAG_FAM):
                i += 1



    