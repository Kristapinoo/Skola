from tracemalloc import start


kvadrats={}
for n in range(5):
    kvadrats[str(n)]=n*n
print(kvadrats)

kubs={f"kubs no {n}": n**3 for n in range(1, 8)}
print(kubs)

ediens="kartupelis"
abc="abcdefghij"
jauns={k:v for k,v in zip(ediens,abc)}
print(jauns)

jauns2={k:v for k,v in enumerate(ediens)} # sanumurē sākot ar 0
print(jauns2)

jauns3={k:v for k,v in enumerate(ediens,start=1)} # sanumurē sākot ar skaitli, kas ir aiz start=
print(jauns3)

paara={n:"vērtība "+str(n) for n in range(1,11) if n%2==0} #izprintē pāra skaitļus
print(paara)

dog=[{"Šķirne":"taksis", "vārds":"Čika"}, {"Šķirne":"buldogs", "vārds":"bobis"}] #saraksts kopā ar vārdnīcu
print(dog)
print(dog[1]) #izprintēja pirmo sarakstā