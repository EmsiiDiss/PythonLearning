from datetime import datetime

liczba = 1
wynik = 0

def prime_numver():
    global liczba, wynik
    date1 = datetime.now()
    while liczba <= 100000:
        for i in range(2,int(liczba/2)+1):
            if liczba%i == 0:
                wynik = wynik + 1
                break

        if wynik == 0:
            print(liczba)
        wynik = 0
        liczba = liczba + 1
    date2 = datetime.now()
    czas_minuty = int((date2 - date1).total_seconds()/60)
    czas_sekundy = int((date2 - date1).total_seconds()%60)
    print("Czas obliczen = " + str(czas_minuty) + ":" + str(czas_sekundy))  

try:
    prime_numver()
except KeyboardInterrupt:
    print("XD")    