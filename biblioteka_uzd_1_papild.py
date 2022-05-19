class Rekins:
    klients = input('Ievadi savu vārdu')
    veltijums = input('Ievadi veltījuma tekstu')
    garums = int(input('Ievadi lādītes garumu milimetros'))
    platums = int(input('Ievadi lādītes platums milimetros'))
    augstums = int(input('Ievadi lādītes augstumu milimetros'))
    izmers = (garums, 'x', platums, 'x', augstums)
    materials = float(input('Ievadi kokmateriāla cenu EUR/m2'))
    
    def izdrukat():
        
