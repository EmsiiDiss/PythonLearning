napis = "Ala ma kota, a kot ma Ale"

lista_napis = list(napis)
napis_odw = []
for id in range(len(lista_napis), 0, -1):
    napis_odw.append(lista_napis[id-1])

print(''.join(napis_odw))


for id in range(len(lista_napis) // 2):
    lista_napis[id], lista_napis[-id-1] = lista_napis[-id-1], lista_napis[id]
print(''.join(napis_odw))