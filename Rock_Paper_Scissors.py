# Author: Emsii 
# Date: 26.10.2022 
# https://github.com/EmsiiDiss

import random
odstep = ' ' *60
wynik_gracza = 0
wynik_weza = 0
wynik_remis = 0

def main():
    while True:
        wybor_losowy = int(random.randint(1, 3))
        #print(wybor_losowy)
        print("Wybierz coś ciekawego ;)")
        try:
            wybor_user = int(input("1. Papier\n2. Kamień\n3. Nożyczki\n"))
        except:
            main()

        wynik = wybor_losowy - wybor_user

        if wynik == 0:
            remis()
        elif wynik == -1 or wynik == 2:
            przegrana()
        elif wynik == -2 or wynik == 1:
            wygrana()
        else:
            print("Coś poszło nie tak repet")
            main()

def wygrana():
    global wynik_gracza
    print(odstep +"Brawo ruski bawole, udało Ci się mnie pokonać ^^\n " + odstep + "WYGRANA")
    wynik_gracza = wynik_gracza + 1
    print(odstep + "Wygrane:Przegrane:Remisy")
    print(odstep + str(wynik_gracza) + ":" + str(wynik_weza) + ":" + str(wynik_remis))
def przegrana():
    global wynik_weza
    print(odstep +"Brawo ruski bawole, PRZEGRAŁEŚ XD \n " + odstep + "PRZEGRANA")
    wynik_weza = wynik_weza + 1
    print(odstep + "Wygrane:Przegrane:Remisy")
    print(odstep + str(wynik_gracza) + ":" + str(wynik_weza) + ":" + str(wynik_remis))
def remis():
    global wynik_remis
    print(odstep +"Wielkie procesory myślą podobnie ;)\n " + odstep + "REMIS")
    wynik_remis = wynik_remis + 1
    print(odstep + "Wygrane:Przegrane:Remisy")
    print(odstep + str(wynik_gracza) + ":" + str(wynik_weza) + ":" + str(wynik_remis))

try:
    main()
except KeyboardInterrupt:
    print("STOP")    
except:
    print("Oj chyba coś źle wpisałeś")
    main()    
