def change():
    expense = 23.75
    money = 100
    print ("Ingresar gasto:")
    print (expense)
    print ("Dinero recibido")
    print (money)
    print ("\n" + "Vuelto")
    print ("\n" + "Pesos:")
    pesos = int(money - expense)
    print (f"{pesos}")
    vuelto = float(money - expense)
    centavos = ((vuelto - pesos) * 100)
    print ("Centavos:")
    print (int(centavos))
change ()
