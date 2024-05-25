import random

n = 4
kod = []
for i in range(n):
    a = str(random.randint(0, 9))
    while a in kod:
        a = str(random.randint(0, 9))
    kod.append(a)  
print(kod)      
liczba_porob = 0

while True:
    kod_test = input("Podaj 4 cyfry: ")
    kod_test = list(kod_test.strip())
    liczba_porob += 1
    if kod_test != kod:
        for i in range(4):
            if kod_test[i] == kod[i]:
                print(f"Liczba {kod_test[i]} jest na swoim miejscu")
            elif kod_test[i] in kod:
                print(f"Liczba {kod_test[i]} jest w kodzie")
    else:
        print(f"Wygrałeś! Wykonałeś {liczba_porob} prób!")
        break    
 