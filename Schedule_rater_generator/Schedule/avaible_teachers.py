from .Teacher import Teacher
from .Subject import Subject


#You can add as many teachers as you wish to generate from.
# First paramether First name
# Second paramether Last name
try:

    teachers = [
    Teacher("Aleš","Novotný",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Barbora","Novotná",[ Subject("Anglický Jazyk"), Subject("Tělesná výchova"),]),
    Teacher("Brumbál","Ohnivý",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
    Teacher("Libor","Lisoň",[ Subject("Matematika"), Subject("Tělesná výchova"),]),
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
