import imp


import math
def maksa(vajadzigais):
    cena = vajadzigais * linolejs
    return cena

print("Ievadiet lūdzu skaitļus metros un decimālskaitļu starpā liekat '.'")
a = float(input("Ievadi istabas garumu\n"))
b = float(input("Ievadi istabas platumu\n"))
laukums= a * b
vajadzigais = laukums
pari = vajadzigais - laukums
linolejs = float(input('Ievadi linoleja cenu m2, kāds ir veikalā\n'))
print("Jums būs nepieciešams" ,laukums, "m2 linoleja")
print('Kopējām izmaksām vajadzētu būt ' + str(math.ceil(maksa(laukums))))
print('Pāri no nopirktā paliks', pari)

