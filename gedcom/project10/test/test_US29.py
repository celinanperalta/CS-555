import pprint

def test_US29(): 
    
    h = Individual("I4", "H", "M", birth=gedcom_date_to_datetime("1 JAN 1977"), death = gedcom_date_to_datetime("12 FEB 1997"))
    w = Individual("I5", "W", "F", birth=gedcom_date_to_datetime("1 JAN 1977"))

    m = Individual("I6", "M", "P", birth=gedcom_date_to_datetime("1 JAN 1977"),death = gedcom_date_to_datetime("22 JAN 2000"), fams = "F02")
    p = Individual("I7", "J", "W", birth=gedcom_date_to_datetime("1 JAN 1977"), fams = "F02")

    individuals = [h,w, m, p]

    deaths = check_US32(individuals)
    #print(couples)

    assert len(deaths) == 2