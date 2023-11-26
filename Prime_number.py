# Author: Emsii 
# Date: 26.10.2022 
# https://github.com/EmsiiDiss



from datetime import datetime

def main():
    global wynik, liczba
    wynik = 0
    liczba = 0
    odstep = " " *16
    liczba = int(input("Podaj proszę liczbę do sprawdzenia = \n"))
    print("Start...")
    date1 = datetime.now()
    if liczba > 1:
        for i in range(1, liczba + 1):
            test = liczba%i
            if test == 0:
                wynik = wynik + 1
                print(i)
                if szukanie == 0:
                    break   
            if i >= (liczba/2)+1:
                wynik = wynik + 1
                print(liczba)
                break

        if wynik < 1:
            print(odstep + "Liczba 1")  
        else:
            print(odstep + "Liczba nie jest 1")
            print("Liczba %r posiada conajmniej %r dzielniki/ów" % (liczba, wynik))
            date2 = datetime.now()
            czas_minuty = int((date2 - date1).total_seconds()/60)
            czas_sekundy = int((date2 - date1).total_seconds()%60)
            print("Czas obliczen = " + str(czas_minuty) + ":" + str(czas_sekundy))

    else:
        print("Liczba %r jest liczbą pierwsza" % liczba)
    temperaturka()

    repet = input(odstep + "Jeszcze raz? y/n\n")
    if repet == "y" or repet == "Y":
        print("Okay!")
        main()
    else:
        print("Bye!")

def temperaturka():
    try:
        from gpiozero import CPUTemperature
        temperatura = " T RasPI = " + str(CPUTemperature().temperature)[0:4] + "*C "
        print(temperatura)
    except:
        print("Brak czujnika temperatury")      

try:
    szukanie = int(input("Włączyć szukanie dzielników? 1/0\n"))
    main()
except KeyboardInterrupt:
    temperaturka()
    print("Wcześneij zakończono...")
    print("Znaleziono jak dotąd %r dzielniki/ów liczby %r " % (wynik,liczba))
        