#Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii {’A’, ’B’, ’C’, ’D’}.
arr = ["A","B", "C","D"]
for i in range(len(arr)):
    for x in range(i+1, len(arr)):
        print(f'{arr[i]} {arr[x]}')