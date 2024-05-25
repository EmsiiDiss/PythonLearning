zbior = []
a = float(input("Podaj liczbe do zbioru: "))
zbior.append(a)
while a >= 0:
    a = float(input("Podaj liczbe do zbioru: "))
    zbior.append(a)
print(zbior)    

zbior = []
while True:
    a = float(input("Podaj liczbe do zbioru: "))
    if a < 0:
        print(zbior)
        break

a = [1, 2, 4, 5, 7, 9]

for num in a:
    if num % 2 == 0:
        continue #przeskocz 1 wartosc
    print(num)