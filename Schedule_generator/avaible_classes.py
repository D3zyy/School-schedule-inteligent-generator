from Class import Class



#You can add as many classes as you wish to generate from.
# First paramether LOCATION
# Second paramether ID(number)
try:
    classes = [
    Class("First floor",5),
    Class("Second floor",8),
    Class("Third floor",1),
    Class("Fourth floor",2),
    Class("Third floor",27),
    Class("First floor",9),
    Class("First floor",11),
    Class("Fourth floor",14),
    Class("Fourth floor",18),
    Class("Third floor",22),
    Class("Second floor",26),
    ]

except ValueError as e:
    print(e)

except:
    print("An Error occured!")