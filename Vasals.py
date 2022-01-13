from math import*

def aprLaukums(r):
    S=pi*r*r
    return S

# r1=int(input('Ievadiet riņķa rādiusu\n'))
# rez1=aprLaukums(r1)
# r2=int(input('Ievadiet riņķa rādiusu\n')) \\
# rez2=aprLaukums(r2)
# print("Laukumi ir ar pirmo r", rez1, "un ar otro", rez2)

for r in range(1,10,2):
    rez=aprLaukums(r)
    print("Laukums ar r ",r," ir ", round(rez, 2))
