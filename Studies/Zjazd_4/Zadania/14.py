napis = "Ala ma kota,   a kot ma Ale"
napis = napis.split()

#rozwiażanie mało wydajnościowe \/
napis_mod = ""

for i, napis in enumerate(napis):
    if i % 2 == 0:
        napis_mod += napis.lower()
    else:
        napis_mod += napis.upper()

    napis_mod += " "     

print(napis_mod)

#rozwiażanie poprawione \/
napis = "Ala ma kota,   a kot ma Ale"
napis = napis.split()
napis_mod = []

for i, napis in enumerate(napis):
    if i % 2 == 0:
        napis_mod.append(napis.lower())
    else:
        napis_mod.append(napis.upper())

print(" ".join(napis_mod))   
