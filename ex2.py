'''
PROGRAMEAZĂ! Scrieţi un program care citeşte de la tastatură elementele
mulţimilor A şi B şi afişează pe ecran:
a) intersecţia mulţimilor A şi B;
b) reuniunea mulţimilor A şi B;
c) diferenţa mulţimilor A şi B;
Mulţimile A şi B sunt formate din literele mari ale alfabetului latin
'''

def readArr(number):
    a,b=[],[]

    for i in range(number):
        x = input("Press / to stop array addition: ")
        if i == 0:
            a.append(x)
        else:
            b.append(x)
        while x != "/":
            x = input("Press / to stop array addition: ")
            if x != "/":
                if i == 0:
                    a.append(x)
                else:
                    b.append(x)
    c = [a,b]
    return c;
arrs = readArr(2);
#a 
print(arrs[0]+ arrs[1]) 
#b
for a in arrs[0]:
    if a in arrs[1]:
        print("element din intersectie este = "+ a)
#c
for a in arrs[0]:
    if not(a in arrs[1]):
        print("element din diferenta multimilor este = "+ a)


