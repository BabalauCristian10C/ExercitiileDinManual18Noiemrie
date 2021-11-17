#Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii {1, 2, 3, 4}
arr = [1,2,3,4]
for i in range(len(arr)):
    for x in range(i+1, len(arr)):
        print(f'{arr[i]} {arr[x]}')
