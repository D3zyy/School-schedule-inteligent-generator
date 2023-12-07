from .Teacher import Teacher
from .Subject import Subject


#You can add as many teachers as you wish to generate from.
# First paramether First name
# Second paramether Last name
try:

    teachers = [
    Teacher("Ondřej","Mandík",[ Subject("Programové vybavení")]),
    Teacher("Tomáš","Juchelka",[ Subject("Anglický Jazyk")]),
    Teacher("Pavel","Lopocha",[ Subject("Tělesná výchova")]),
    Teacher("Lucie","Brčáková",[ Subject("Podnikové informační systémy"), Subject("Ekonomika"),Subject("Zaklady přirodních věd")]),
    Teacher("Bedřich","Mohutný",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Alžběta","Malá",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Klára","Krátká",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Anna","Mladá",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Lubomír","Zelený",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Harry","Hanák",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Jasmína","Trávníčková",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    ]
except ValueError as e:
    print(e)

except:
    print("An Error occured!")
