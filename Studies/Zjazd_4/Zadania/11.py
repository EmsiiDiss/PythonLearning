a = input("Podaj liczbę: ")
suma = 0

for i in range(len(a)):
    suma += int(a[i])
print(suma)

#to samo
suma = 0
a = int(a)
while a > 0:
    suma += a % 10
    a //= 10
print(suma)