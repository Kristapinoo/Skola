from math import*
def summa(a,b):
    return a+b
a=int(input('Ievadi a skaitli\n'))
b=int(input('Ievadi b skaitli\n'))
y=((summa(a,b)**2)+(4*(summa(a,b))))/(sqrt(summa(a,b)))
y=float(y)
print('Atbilde ir ', y)
