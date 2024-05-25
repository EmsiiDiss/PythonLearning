napis = input("Podaj napis: ")

print("Długość:", len(napis))

print("Czwarty:", napis[3])

print("Przedostatni:", napis[-2])

print("Pierwsze 10:", napis[:10])

print("Wszystkie oprócz ostatnich 5:", napis[:-5])

print("Wszystkie od 5 do 5 od końca:", napis[-5:])

print("Znaki o indeksach parzystych w odwrotnej kolejności:", napis[::-2])
