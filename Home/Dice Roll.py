# Author: Emsii 
# Date: 13.12.2022 
# https://github.com/EmsiiDiss

import random
from datetime import datetime

odstep = " " *8
min_val = 1
max_val = 6

def reset():
    global ilosc, liczba_1, liczba_2, liczba_3, liczba_4, liczba_5, liczba_6, kostka_sr, min_val, max_val, odstep, ile_razy 
    liczba_1 = 0
    liczba_2 = 0 
    liczba_3 = 0 
    liczba_4 = 0 
    liczba_5 = 0
    liczba_6 = 0
    kostka_sr = 0
    ilosc = 0  
    ile_razy = 1

def liczba_roli():
    try:
        ile_razy = int(input(odstep + "Ile razy chcesz rolować?\n"))
    except ValueError:    
        ile_razy = 1
    baza(ile_razy)

def statystyki(statystyka, kostka, start):
    global ilosc, liczba_1, liczba_2, liczba_3, liczba_4, liczba_5, liczba_6, kostka_sr

    kostka_sr = (kostka_sr + kostka)
    if statystyka == 1 or statystyka == 2:    
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
 
    if (statystyka == 1 or statystyka == 2) and start != 1:                                    
        date2 = datetime.now()
        czas_minuty = int((date2 - date1).total_seconds()/60)
        czas_sekundy = int((date2 - date1).total_seconds()%60)
        print("""
Statystyki:
        1-%r
        2-%r
        3-%r
        4-%r
        5-%r
        6-%r""" 
        % (liczba_1,liczba_2,liczba_3,liczba_4,liczba_5,liczba_6)
        )
        print("Średnio wypadało oczkek = " + str(kostka_sr / ilosc)[0:4])
        print("Czas obliczeń = " + str(czas_minuty) + ":" + str(czas_sekundy))


def baza(ile_razy):
    global statystyka, date1, ilosc
    date1 = datetime.now()
    for i in range(0,ile_razy):
        kostka = random.randint(min_val,max_val)
        ilosc = ilosc + 1
        statystyki(statystyka, kostka, 1)
        print(char[kostka-1])     
        print("Kostka wylosowała = " + str(kostka)+"\n")
        

    statystyki(statystyka, 0, 0)
    resecik = input("Jeszcze raz? y/n\n")
    if resecik == "y" or resecik == "Y" or resecik == '':
        if statystyka != 2:
            reset()
        print("Okay!")
        liczba_roli()
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

def main():
    reset()
    try:
        global statystyka
        print("""
            0 - brak statystyki,
            1 - statystyka miękka,
            2 - statystyka twarda,
        """)
        statystyka = int(input(odstep + "Włączyć statystykę? 2/1/0\n"))
        
    except:
        print("Źle coś wprowadziłeś/aś - statystyka WYŁĄCZONA") 
        statystyka = 0
    statystyki(statystyka,0,1)
    liczba_roli()

try:
    main()
except KeyboardInterrupt:
    statystyki(2,0,0)
    print("XDDD")            