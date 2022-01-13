from math import*
def izt(a,b):
    return ((a*b)+(a/b))

a=int(input('Ievadi a skaitli\n'))
b=int(input('Ievadi b skaitli\n'))
x=(izt(a,b)+(6*izt(a,b))-(izt(a,b)**2))/(izt(a,b))
print(x)