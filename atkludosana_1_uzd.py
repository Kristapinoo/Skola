# Sula veikalā maksā 1.50 eiro (bez PVN) un siers 3 eiro (bez PVN). 
# Aprēķini, cik kopā tev ir jāmaksā par pirkumu ar PVN!

PVN = 0.21

sulasCena = 1.00
sulasPVN = sulasCena * PVN

sieraCena = 3.00
sieraPVN = sieraCena * PVN

print(sulasCena + sulasPVN + sieraCena + sulasPVN)

