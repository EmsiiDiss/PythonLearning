from datetime import datetime
from tabulate import tabulate

def sumowanie(liczba):
    dlugosc = len(str(liczba))
    suma = 0
    miejsce = 0
    for i in range(0,dlugosc):
        suma = suma + int(str(liczba)[-miejsce])
        miejsce = miejsce + 1
    return suma

def prime_numver(dolna, gorna):
    wynik = 0
    liczba_pierwszych = 0
    for sprawdzana in range(dolna, gorna):
        ost_liczba = int(str(sprawdzana)[-1])
        if ost_liczba == 0 or ost_liczba == 2 or ost_liczba == 4 or ost_liczba == 6 or ost_liczba == 8 or sumowanie(sprawdzana) % 3 == 0:
            wynik = wynik + 1

        elif wynik == 0:
            for i in range(2,int(sprawdzana/2)+1):
                if sprawdzana%i == 0:
                    wynik = wynik + 1
                    break
            if wynik == 0:
                print((" "*19)+str(sprawdzana))
                liczba_pierwszych = liczba_pierwszych + 1
        wynik = 0
    print("Znaleziono liczb pierwszych w zakresie", dolna, "-", gorna, ":", liczba_pierwszych)


def main():
    print("Podaj zakres liczb do sprawdzenia \n a > 1 \n b > 1\n")
    liczba_1 = int(input("Podaj 1 liczbe \n"))
    liczba_2 = int(input("Podaj 2 liczbe \n"))

    date1 = datetime.now()
    if liczba_1 > 1 and liczba_2 > 1:
        if liczba_1 > liczba_2:
            prime_numver(liczba_2, liczba_1)
        else:
            prime_numver(liczba_1, liczba_2)
    else:
        print("Za maly zakres")
        main()

    date2 = datetime.now()
    czas_minuty = int((date2 - date1).total_seconds()/60)
    czas_sekundy = int((date2 - date1).total_seconds()%60)
    czas_ms = round((date2 - date1).microseconds/1000, 0)
    timer = [['', 'Minutes', 'Seconds', 'Millisecond'], ["Calculation time", czas_minuty, czas_sekundy, czas_ms]]
    print(tabulate(timer, headers='firstrow', tablefmt='fancy_grid'))

try:
    main()
except KeyboardInterrupt:
    print("XD")