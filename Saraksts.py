def izdruka(daudzums, sar1):
    for elementi in range(0, daudzums):
        print(sar1[elementi])
    #return 

sar1=[1,2,3,4,5,6,7,8,9,10]
daudzums=int(input('Norādiet daudzumu\n'))
rezultāts=izdruka(daudzums, sar1) 
print(rezultāts)