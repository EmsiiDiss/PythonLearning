# Author: Emsii 
# Date: 12.12.2022 
# https://github.com/EmsiiDiss

import random

odstep = " " *16

def start():
    global liczba, Wynik_start, minimum, maksimum
    print("\nHey, zagrajmy w grę - zgadnij o jakiej liczbie myślę ;)\n")
    try:
        print("W jakim zakresie ma być gra?")
        minimum = int(input("Wartość minimalna?\n"))
        maksimum = int(input("Wartość maksymalna?\n"))
        liczba = int(random.randint(minimum, maksimum))
        print(odstep+"Niech zaczną się igrzyska XD")
        Wynik_start = maksimum - minimum
    except ValueError:
        print("Oj chyba nie XD - podaj liczbe")    
    zgadywanie()

def zgadywanie():
    global moja_liczba,Wynik
    Wynik = Wynik_start
    while True:
        try:
            moja_liczba = int(input("Podaj proszę liczbę, o której myślę ;)\n" + odstep + "(Pamiętaj idioto -- z zakresu %r - %r)\n" % (minimum, maksimum)))
            
            if moja_liczba == liczba:
                print("\n"+odstep+"Brawo Turbanie udało Ci się XD")
                print("Wynik = " + str(int(Wynik/Wynik_start*100))+"%")
            
                retry = input(odstep+"Jeszcze raz? Yes/No\n")
                if retry == "Yes" or retry == "yes":
                    start()
                elif retry == "no" or retry == "No":
                    break
                else:
                    print("Foch nie potrafisz nawet odpowiedzieć na proste pytanie -_-'\n Paaa!!!\n")
                    break

            elif moja_liczba <= liczba:
                Wynik = Wynik - 5
                print("\n"+odstep+"No nie tym razem")
                print(odstep*5+"Liczba o której myśle jest większa :/")
                print(odstep+"Wynik = " + str(int(Wynik/Wynik_start*100))+"%")

            elif moja_liczba >= liczba:
                Wynik = Wynik - 5
                print("\n"+odstep+"No nie tym razem")
                print(odstep*5+"Liczba o której myśle jest mniejsza :/")
                print(odstep+"Wynik = " + str(int(Wynik/Wynik_start*100))+"%")

        except ValueError:
            print("Oj chyba nie XD - podaj liczbe")
                
try:
    start()
except KeyboardInterrupt:
    print("XDDD")                
