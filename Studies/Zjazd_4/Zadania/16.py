list_1= [1, 3, 4, 6, 7, 8]
list_2= [3, 6, 7, 4, 2, 1, 5]
 
for a, b in zip(list_1, list_2):
    print(f"{a} + {b} = {a + b}")