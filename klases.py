# class person:
#     def set(self,name,age): #metodes definēšana
#         self.name = name # šeit tiek izveidots lauks name
#         self.age = age # šeit tiek izveidots lauks age
#     def output(self): # metodes definēšana
#         print(self.name,self.age)

# p = person() # objekta izveidošana
# p.set("Peter", 20)
# p.output()

#                   VAI

# class person:
#     def set(self,name,age): #metodes definēšana
#         self.name = name # šeit tiek izveidots lauks name
#         self.age = age # šeit tiek izveidots lauks age
#     def output(self): # metodes definēšana
#         print(self.name,self.age)

# p = person() # objekta izveidošana
# person.set(p,"Peter" , 20)
# person.output(p)

#                   VAI

# class person:
#     pass # klasē nekā nav

# p = person() # objekta izveidošana
# p.name = "Peter" # lauka name izveidošana no ārpuses
# p.age = 20 # lauka age izveidošana no ārpuses
# print(p.name, p.age)

# SLĒPTO (PRIVATE) ELEMENTU DEFINĒŠANA

# class person:
#     def set(self,name,age): # metodes definēšana
#         self.__name = name # šeit tiek izveidots slēptais lauks name
#         self.__age = age # šeit tiek izveidots slēptais lauks age
#     def output(self): # metodes definēšana
#         print(self.__name, self.__age)

# p = person() # objekta izveidošana
# p.set("Peter", 20)
# print(p.__name) # nevar piekļūt slēptajam laukam, izmet kļūdu
# p.output()

# NEATĻAUJ PIEKĻŪT IEVADĪTAJAI INFORMĀCIJAI, NEPRINTĒ ĀRĀ, BET MET ERROR

# PIEKĻUVE SLĒPTAJAM LAUKAM SPECIFISKI VAI NETIEŠI

class person:
    def set(self,name,age):
        self.__name = name
        self.__age = age
    def output(self):
        print(self.__name,self.__age)

p = person()
p.set("Peter", 20)
print(p._person__name) # var piekļūt slēptajam laukam šādi
p.output() # var piekļūt slēptajam laukam caur metodi

