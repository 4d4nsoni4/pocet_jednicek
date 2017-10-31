#cislo = input("Zadej číslo: ")

#pocet_jednicek = cislo.count('1')
        #formátovaný zápis, závorky mi ukazaují na místo, kde bude proměnná, pak v x.format(a, b, c) se mi to doplní, viz 05
#print("Počet jedniček v cisle {} je {}.".format(cislo, pocet_jednicek))

def pocet_jednicek(cislo):
    """ spočítá počet jedniček v čísle """
    pocet = 0
    # if cislo < 0:
    #     cislo = -cislo
    cislo = abs(cislo)
    while abs(cislo) > 0:
        zbytek = cislo % 10
        if zbytek == 1:
            pocet = pocet + 1
        cislo = cislo // 10
    return pocet

cislo = int(input("Zadej číslo: "))
pocet = pocet_jednicek(cislo)
print("Počet jedniček v čísle {} je {}.".format(cislo, pocet))
