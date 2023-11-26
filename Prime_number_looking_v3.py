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

def prime_numver(liczba):
    wynik = 0
    date1 = datetime.now()
    for sprawdzana in range(1, liczba):
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

        wynik = 0

    date2 = datetime.now()
    czas_minuty = int((date2 - date1).total_seconds()/60)
    czas_sekundy = int((date2 - date1).total_seconds()%60)
    czas_ms = round((date2 - date1).microseconds/1000, 0)
    timer = [['', 'Minutes', 'Seconds', 'Millisecond'], ["Calculation time", czas_minuty, czas_sekundy, czas_ms]]
    print(tabulate(timer, headers='firstrow', tablefmt='fancy_grid'))

try:
    liczba = 15677
    prime_numver(liczba)
except KeyboardInterrupt:
    print("XD")