from util import gedcom_date_to_datetime


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
        self.name = name.replace("/", "")

    def set_sex(self, sex):
        self.sex = sex
    
    def set_birth(self, birth):
        self.birth = gedcom_date_to_datetime(birth)
    
    def set_death(self, death):
        self.death = gedcom_date_to_datetime(death)
    
    def set_famc(self, famc):
        self.famc = famc

    def set_fams(self, fams):
        self.fams = fams

    def to_table_row(self):
        return [self.id, self.name, self.sex, self.birth, self.death, self.famc, self.fams]

    def __str__(self):
        return f"{self.name} ({self.id})"

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
        self.marriage_date = gedcom_date_to_datetime(marriage_date)

    def set_divorce_date(self, divorce_date):
        self.divorce_date = gedcom_date_to_datetime(divorce_date)

    def add_child(self, child):
        self.children.append(child)

    # For pretty printing families
    def to_table_row(self):
        return [self.id, self.husband.name, self.wife.name, [x.id for x in self.children], self.marriage_date, self.divorce_date]
    
    def __str__(self):
        return f"{self.id} {self.husband.name} {self.wife.name}"

