import math
def maksa(vajadzigais):
    cena = vajadzigais * linolejs
    return cena

print("Ievadiet lūdzu skaitļus metros un decimālskaitļu starpā liekat '.'")
a = float(input("Ievadi istabas garumu\n"))
b = float(input("Ievadi istabas platumu\n"))
laukums= a * b
vajadzigais = round(math.ceil(laukums),2)
pari = round(math.ceil(laukums),2) - laukums
linolejs = float(input('Ievadi linoleja cenu m2, kāds ir veikalā.\n'))
print("Jums būs nepieciešams" ,round(laukums, 2), "m2 linoleja. Sanāk jums būs jāpērk", round(math.ceil(laukums),2), "m2")
print('Kopējām izmaksām vajadzētu būt', round(maksa(vajadzigais), 2), 'EUR')
print('Pāri no nopirktā linoleja būs', round(pari, 2), 'm2')