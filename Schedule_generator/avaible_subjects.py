from Subject import Subject


#You can add as many subjects as you wish to generate from.
# First paramether name

try:
    subjects = [
        Subject("Matematika"),
        Subject("Tělesná výchova"),
        Subject("Anglický Jazyk"),
        Subject("Český Jazyk"),
        Subject("Cvičení ze správy IT"),
        Subject("Webové aplikace"),
        Subject("Databázové systémy"),
        Subject("Technický projekt"),
        Subject("Programové vybavení"),
        Subject("Aplikovaná matematika"),
        Subject("Podnikové informační systémy"),
        Subject("Počitačové systémy a sítě"),



    ]





except ValueError as e:
    print(e)

except:
    print("An Error occured!")

