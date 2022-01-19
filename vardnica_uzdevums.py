suns={"šķirne":"dalmācietis", "vārds":"antons", "svars": 14.2}
for key in suns.keys():
    print(key,end=", ")
for value in suns.values():
    print(value,end=", ")
print()
for key, value in suns.items():
    print(key, "=", value,end=", ")