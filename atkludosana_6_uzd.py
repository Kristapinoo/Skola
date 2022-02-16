# Lietotājs ievada vairākus skaitļus, atdalot tos ar atstarpi. 
# Izvadi lielākā ievadītā skaitļa vērtību un indeksu sarakstā!

skaitli = [int(skaitli) for skaitli in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

lielIndex = 0

for i in range(1, len(skaitli)):
    if skaitli[i] > skaitli[lielIndex]: 
        lielIndex = i

print(f"Lielakais skaitlis: {skaitli[lielIndex]} ar indeksu {lielIndex}")
