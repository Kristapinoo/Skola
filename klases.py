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

# class person:
#     def set(self,name,age):
#         self.__name = name
#         self.__age = age
#     def output(self):
#         print(self.__name,self.__age)

# p = person()
# p.set("Peter", 20)
# print(p._person__name) # var piekļūt slēptajam laukam šādi
# p.output() # var piekļūt slēptajam laukam caur metodi

# class person:
#     def __init__(self, name, age): # konstruktora definēšana
#         self.name = name
#         self.age = age
#     def output(self):
#         print(self.name, self.age)

# p = person("Peter", 20)

# p.output()

# class person:
#     def __init__(self, name, age): # konstruktora definēšana
#         self.name = name
#         self.age = age
#     def output(self):
#         print(self.name, self.age)
#     def __del__(self):
#         print("Deleted:", self.name, self.age)

# p = person("Peter", 20)

# p.output()
# del p # objekta likvidēšana un attiecīgi destruktora izsaukšana

class person:
    counter = 0 # klases līmeņa lauks
    def __init__(self,name,age):
        self.name = name
        self.age = age
        person.counter += 1 # klases lauka modifikācija
    def __del__(self):
        person.counter -= 1 # klases laika modifikācija
    def output(self): # instances metode
        print(self.name, self.age)
    @classmethod
    def output_counter(cls): # klases līmeņa metode
        print(cls.counter)

person.output_counter() # objektu skaits 0
p1 = person("Liz", 19)
p1.output()
p1.output_counter() # objektu skaits 1
p2 = person("Peter", 20)
p2.output()
p2.output_counter() # objektu skaits 2
p1 = None
p2 = None
person.output_counter() # objektu skaits 0