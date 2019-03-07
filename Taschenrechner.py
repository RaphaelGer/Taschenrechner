#Also ich habe einen Taschenrechner programmiert der + - * / ausführen kann und am ende alle ergebnisse plus aufgabe ausgebe
#erkläre dem user das es sich um einen taschenrechner handelt
print("Hallo, ich bin dein Taschenrechner !")
#definiere die erste variable die der user eingeben kann
x = 0
#die zweite variable
y = 0
#ergebnis und die rechnung speichern in einer liste
Ergebnisse = []
#sollange True führe die schleife aus
again = True

while again == True:
# frage den user nach den variablen und den operator
    x = input("Was ist deine erste Zahl: ")
    op = input("Was ist dein operator: ")
    y = input("Was ist deine zweite Zahl: ")

    if op == "/":
        erg = float(x) / float(y)
        # ergebnis ausgeben
        print(erg)
        # ergebnis + rechnung der liste hinzufügen
        Ergebnisse.append(x +" / "+ y +" = " + str(erg))
        # will er noch eine Rechnung ausführen ?
        print("Hast du noch eine Aufgabe für mich y/n")
        z = input()
        if z == "n":
            again = False
        else:
            again = True
    elif op == "+":
        erg = float(x) + float(y)
        # ergebnis ausgeben
        print(erg)
        # ergebnis + rechnung der liste hinzufügen
        Ergebnisse.append(x +" + "+ y +" = " + str(erg))
        # will er noch eine Rechnung ausführen ?
        print("Hast du noch eine Aufgabe für mich y/n")
        z = input()
        if z == "n":
            again = False
        else:
            again = True
    elif op == "-":
        erg = float(x) - float(y)
        # ergebnis ausgeben
        print(erg)
        # ergebnis + rechnung der liste hinzufügen
        Ergebnisse.append(x +" - "+ y +" = " + str(erg))
        # will er noch eine Rechnung ausführen ?
        print("Hast du noch eine Aufgabe für mich y/n")
        z = input()
        if z == "n":
            again = False
        else:
            again = True
    elif op == "*":
        erg = float(x) * float(y)
        # ergebnis ausgeben
        print(erg)
        # ergebnis + rechnung der liste hinzufügen
        Ergebnisse.append(x +" * "+ y +" = " + str(erg))
        # will er noch eine Rechnung ausführen ?
        print("Hast du noch eine Aufgabe für mich y/n")
        z = input()
        if z == "n":
            again = False
        else:
            again = True
    else:
        print("ungültige eingabe")
        again = False

print("Hier noch mal alle Rechnungen die du eingegeben hast: ")
print(Ergebnisse)
