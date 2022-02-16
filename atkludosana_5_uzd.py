# Lietotājs ievada vairākus skaitļus vienā rindā, atdalot tos ar atstarpi. 
# Izvadi tos skaitļus, kuri ir vienādi un atrodas blakus!

saraksts = [int(sk) for sk in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

for i in range(len(saraksts)):
    if saraksts[i] == saraksts[i + 1]: 
        print(saraksts[i], saraksts[i + 1])
