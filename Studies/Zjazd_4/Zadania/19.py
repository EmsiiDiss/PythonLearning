napis = "Ala ma kota, a Kot ma Ale"
napis = napis.lower()

napis = list(napis.strip())
napis.sort()

counts = {}
for znak in napis:
    if znak.isalpha():
        if znak in counts:
            counts[znak] += 1
        else:
            counts[znak.lower()] = 1

for key in counts.keys():
    print(key, counts[key])