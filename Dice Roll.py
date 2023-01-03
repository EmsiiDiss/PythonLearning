# Author: Emsii 
# Date: 13.12.2022 
# https://github.com/EmsiiDiss

import random
from datetime import datetime

min_val = 1
max_val = 6
odstep = " " *16
ile_razy = 1

def main():
    global ilosc, kostka_sr, ile_razy

    liczba_1 = 0
    liczba_2 = 0 
    liczba_3 = 0 
    liczba_4 = 0 
    liczba_5 = 0
    liczba_6 = 0
    ilosc = 0
    kostka_sr = 0
    try:
        global ile_razy
        ile_razy = int(input(odstep + "Ile razy chcesz rolować?\n"))
    except ValueError:
        pass  

    date1 = datetime.now()
    for i in range(0,ile_razy):
        kostka = random.randint(min_val,max_val)
        ilosc = ilosc + 1

        if statystyka == 1: 
            print("Kostka wylosowała = " + str(kostka))

        kostka_sr= (kostka_sr + kostka)
        if kostka == 1:
            liczba_1 = liczba_1 + 1
        elif kostka == 2:
            liczba_2 = liczba_2 + 1
        elif kostka == 3:
            liczba_3 = liczba_3 + 1
        elif kostka == 4:
            liczba_4 = liczba_4 + 1
        elif kostka == 5:
            liczba_5 = liczba_5 + 1
        elif kostka == 6:
            liczba_6 = liczba_6 + 1 
        print(char[kostka-1])     

    if statystyka == 1:                                                          
        date2 = datetime.now()
        print("1-%r\n2-%r\n3-%r\n4-%r\n5-%r\n6-%r" % (liczba_1,liczba_2,liczba_3,liczba_4,liczba_5,liczba_6))
        print("Średnio wypadało oczkek= " + str(kostka_sr / ilosc)[0:4])
        czas_minuty = int((date2 - date1).total_seconds()/60)
        czas_sekundy = int((date2 - date1).total_seconds()%60)
        print("Czas obliczeń : " + str(czas_minuty) + ":" + str(czas_sekundy))
    resecik = input("Jeszcze raz? y/n\n")
    if resecik == "y" or resecik == "Y" or resecik == '':
        print("Okay!")
        main()
    else:
        
        print("Bye!")

char = [("""
             -------------
            |             |
            |      0      |
            |             |
             -------------
            """),
        ("""
             -------------
            |    0        |
            |             |
            |        0    |
             -------------
            """),
        ("""
             -------------
            |    0        |
            |      0      |
            |        0    |
             -------------
            """),
        ("""
             -------------
            |    0   0    |
            |             |
            |    0   0    |
             -------------
            """),         
        ("""
             -------------
            |    0   0    |
            |      0      |
            |    0   0    |
             -------------
            """), 
        ("""
             -------------
            |    0   0    |
            |    0   0    |
            |    0   0    |
             -------------
            """),                        
        ]

try:
    try:
        statystyka = int(input("Włączyć statystykę? 1/0\n"))
    except:
        print("Źle coś wprowadziłeś/aś - statystyka WYŁĄCZONA") 
        statystyka = 0   
    main()
except KeyboardInterrupt:
    print("XDDD")            