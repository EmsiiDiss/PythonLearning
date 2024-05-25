lista = [4, 26, 8, 2, 64, 326, 897, 123, 245, 5432, 1]
print(max(lista), min(lista), (sum(lista)))

maxi = lista[0]
minimal = lista[0]
suma = 0

for liczba in lista:
    if liczba > maxi:
        maxi = liczba
        index_maxi = lista.index(liczba)
    if liczba < minimal:
        minimal = liczba
        index_minimal = lista.index(liczba)
    suma += liczba    
print(maxi, index_maxi)
print(minimal, index_minimal)
print(suma)
