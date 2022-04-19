# Klases nosaukums

class Robots:
    """Klase reprezentē robotu ar specifisku vārdu"""
    
    #Klases konstruktors. Ar šo metodi tiek inicializēts objekts.
    def __init__(self, vards):
        """Datu inicalizācija."""
        # Īpašības definēšana
        self.vards = vards
        print("(Inicializējam {})".format(self.vards))

    # Metode, kas izvada tekstu
    def iznicinat(self):
        print("{} tiek iznīcināts!".format(self.vards))
    
    # Metode, kas izvada tekstu
    def sasveicinaties(self):
        print("Sveiks! Mani sauc {}.".format(self.vards))

# 1. robota izveide
droid1 = Robots("R2-D2")

# 1. robota metodes pārbaude
droid1.sasveicinaties()

# 2. robota izveide
droid2 = Robots("C-3PO")

# 2.robota metodes pārbaude
droid2.sasveicinaties()

print("\nRoboti šeit var paveikt kādu darbu..\n")
print("Roboti visu ir izdarījuši. Mēs viņus varam iznīcināt.")
droid1.iznicinat()
droid2.iznicinat()