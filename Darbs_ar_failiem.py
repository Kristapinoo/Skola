import encodings


with open ('teksts.txt', encoding= "utf-8") as f:       #utf-8 nozīmē, ka ar latviešu valodas burtiem izpirntēs
    print(f.read())         #izprintēs tekstu no faila

with open ('teksts.txt', encoding= "utf-8") as f:
    for line in f:
        print(line)         #Starp katru rindiņu lielāka atstarpe

with open ('teksts.txt', encoding= "utf-8") as f:
    mylines = f.readlines() # mylines[line.rstrip('/n') for line in f] #izprintēs beigu simboliem, kas ierakstīts iekavaās.
print(mylines[:10])         #Izprintēs rindas sarakstā. Skaitlis 10 nozīmē cik rindas ņems teksta

with open ('teksts.txt', encoding= "utf-8") as f:
    filtrs=[line.rstrip('/n') for line in f if "stipendija" in line]    #Izdrukā visus teikumus kurā ir šis vārds, kas ir "..."
    filtrs1=[line.rstrip('/n') for line in f if line.startswith("Zinu")]    #Izprintēs visus teikumus, kuri sākas ar vārdu, kas ir "..."

with open ('teksts.txt', encoding= "utf-8") as f:
    filtree_linijas = [] #Šeit viss sākas ar izvēlētā vārda saraksta izveidošanu
    for line in f:
     if line.startswith("Tests"):
         filtree_linijas.append(line)
print(filtree_linijas)

with open('teksts_papildinats.txt', mode = "w", encoding = 'utf-8') as f: #Šeit izvēlētā saraksta vērtības tiek izveidotas jaunā failā
    f.writelines(filtree_linijas)

#with open('teksts_papildinats.txt', mode = "a", encoding = 'utf-8') as f: #Šeit izvēlētā saraksta vērtības tiek pievienota klāt jaunajā failā
#   f.writelines(filtree_linijas)
# w - iesāk jaunu failu
# a - papildina iesākto jauno failu

with open ('teksts.txt', encoding="utf-8") as fin, open("cits.txt", encoding="utf-8", mode="w") as font: # viss tas pats, kas iepriekš tikai vienā rindā
    for line in fin:
        if line.startswith("Tests"):
            font.write(line)