a = int(input("Podaj loczbę: "))

if a % 2 == 0:
    print(f'Liczba {a} jest parzysta')

else:
    print(f'Liczba {a} jest nieparzysta')


if a > 0:
    print(f'Liczba {a} jest dodatnia')
elif a < 0:
    print(f'Liczba {a} jest ujemna')
else:
    print(f'Liczba {a} jest zerem')    

i = 0
while i < 5:
    print(i)
    i += 1    

#range(start, stop, step)
for i in range (0, 5, 0):
    print(i)