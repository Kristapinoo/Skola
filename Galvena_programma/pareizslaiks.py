def pareizslaiks():
    import datetime
    now = datetime.datetime.now()
    print("Šodienas Datums un Laiks ir : ")
    print(now.strftime("%d-%m-%Y %H:%M:%S"))