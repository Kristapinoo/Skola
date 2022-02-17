def parisNeparis():
    ievadsSkaitlis = int(input("Ievadiet skaitli:"))
    paris = (ievadsSkaitlis % 2) == 0
    if paris == True:
        print("Skaitlis {0} ir {1} skaitlis".format(ievadsSkaitlis, "Para"))
    else:
        print("Skaitlis {} ir Nepāra skaitlis".format(ievadsSkaitlis))