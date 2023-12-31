from .Teacher import Teacher
from .Subject import Subject


#You can add as many teachers as you wish to generate from.
# First paramether First name
# Second paramether Last name
# third paramether array of subject objects
try:

    teachers = [
    Teacher("Ondřej","Mandík",[ Subject("Programové vybavení")]),
    Teacher("Tomáš","Juchelka",[ Subject("Anglický Jazyk")]),
    Teacher("Pavel","Lopocha",[ Subject("Tělesná výchova")]),
    Teacher("Lucie","Brčáková",[ Subject("Podnikové informační systémy")]),
    Teacher("Libuše","Hrabalová",[ Subject("Matematika")]),
    Teacher("Vladimír","Váňa",[ Subject("Cvičení ze správy IT")]),
    Teacher("Lukáš","Masopust",[Subject("Technický projekt")]),
    Teacher("Kristína","Studenková",[ Subject("Český jazyk")]),
    Teacher("Filip","Kallmunzer",[ Subject("Aplikovaná matematika")]),
    Teacher("Daniel","Adámek",[ Subject("Webové aplikace")]),
    Teacher("Jan","Molič",[ Subject("Počítačové systémy a síťe")])

    ]
except ValueError as e:
    print(e)

except:
    print("An Error occured!")
