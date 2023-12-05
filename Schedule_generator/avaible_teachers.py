from Teacher import Teacher



#You can add as many teachers as you wish to generate from.
# First paramether First name
# Second paramether Last name
try:
    teachers = [
    Teacher("Aleš","Novotný"),
    Teacher("Barbora","Novotná"),
    Teacher("Brumbál","Ohnivý"),
    Teacher("Libor","Lisoň"),
    Teacher("Bedřich","Mohutný"),
    Teacher("Alžběta","Malá"),
    Teacher("Klára","Krátká"),
    Teacher("Anna","Mladá"),
    Teacher("Lubomír","Zelený"),
    Teacher("Harry","Hanák"),
    Teacher("Jasmína","Trávníčková"),
    ]
except ValueError as e:
    print(e)

except:
    print("An Error occured!")
