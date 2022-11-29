from typing import List

from util import gedcom_date_to_datetime, get_age_in_years


class Individual:
    def __init__(
        self, id, name=None, sex=None, birth=None, death=None, famc=[], fams=[]
    ) -> None:
        self.id = id
        self.name = name
        self.sex = sex
        self.birth = birth
        self.death = death
        self.famc = []
        self.fams = []

    def set_name(self, name):
        self.name = name.replace("/", "")

    def set_sex(self, sex):
        self.sex = sex

    def set_birth(self, birth):
        self.birth = gedcom_date_to_datetime(birth)

    def set_death(self, death):
        self.death = gedcom_date_to_datetime(death)

    def set_famc(self, famc):
        self.famc.clear()
        for x in famc:
            self.famc.append(x)

    def add_famc(self, x):
        self.famc.append(x)

    def set_fams(self, fams):
        self.fams.clear()
        for x in fams:
            self.fams.append(x)

    def add_fams(self, x):
        self.fams.append(x)

    def to_table_row(self):
        return [
            self.id,
            self.name,
            self.sex,
            self.birth,
            self.death,
            self.famc,
            self.fams,
            get_age_in_years(self),
        ]

    def __str__(self):
        return f"{self.name} ({self.id})"


class Family:
    def __init__(
        self,
        id,
        husband: Individual = None,
        wife: Individual = None,
        children: List[Individual] = [],
        marriage_date=None,
        divorce_date=None,
    ) -> None:
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
            self.children.sort(key=lambda x: x.birth if x.birth else 0) # US28

    def set_marriage_date(self, marriage_date):
        self.marriage_date = gedcom_date_to_datetime(marriage_date)

    def set_divorce_date(self, divorce_date):
        self.divorce_date = gedcom_date_to_datetime(divorce_date)

    def add_child(self, child):
        self.children.append(child)
        self.children.sort(key=lambda x: x.birth if x.birth else 0)

    # For pretty printing families
    def to_table_row(self):
        return [
            self.id,
            self.husband.name if self.husband else "None",
            self.wife.name if self.wife else "None",
            [x.id for x in self.children],
            self.marriage_date,
            self.divorce_date,
        ]

    def __str__(self):
        return f"{self.id}"
