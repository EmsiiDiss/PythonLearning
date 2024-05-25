list = [1, 9, 4, 49, 16, 36]

for id, elem in enumerate(list):
    if id ** 2 == elem:
        print(f"{id} {elem} Kwadrat!")
    else:
        print(f"{id} {elem}")    

