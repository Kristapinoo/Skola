#{atslēga: vērtība, ...}

# tuksa={}
# tuksa["vards"]=12345678
# a=len(tuksa)
# print(a)
tel={"valdis":12345678, "pēteris":876543421, "līga": 45362718, "Jana":12431244}
# a=len(tel)
# print(a)
tel["Juris"]=21232123
tel["liene"]="meitene"
tel["temperatūra"]=-1.5
print(tel)
atslegas=tel.keys() #1 variants

print(tel.keys()) # 2 variants
print(tel.values())

print(list(atslegas)) # bez dict_... priekšā, tikai kvadrātiekavas
print(list(tel.values())) # tas pats variants
print("valdis" in tel) # var pārbaudīt vai ir vārdnīcā iekšā
print(tel.get("valdis")) #atrod atslēgas vērtību
print(tel.items()) #izdrukā visu vārdnīcu 
del tel["temperatūra"] # izdzēš konkrēto atslēgu
tel.clear() #izdzēš visu sarakstu