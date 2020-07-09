while True:
    print ("MENU
    S. SUMA
    R. RESTA
    M. MULTIPLICACION
    D. DIVISION
    A. SALR
    ")

    opcion= input("ELIGE UNA OPCION: ").upper()

    if opcion == "S" or opcion == "R" or opcion == "M" or opcion =="D":
        
        numero1= int(input("DIME UN NUMERO: "))
        numero2= int(input("DIME OTRO NUMERO: "))

        if opcion == "S":
            print(f'LA SUMA DE LOS NUMEROS ES: {numero1 + numero2}')
        elif opcion == "R":
            print (f'LA RESTA DE LOS NUMEROS ES: {numero1 - numero2}')
        elif opcion == "M":
            print (f'LA MULTIPLICACION DE LOS NUMEROS ES: {numero1 * numero2}')
        elif opcion == "D":
            print (f'LA DIVICION DE LOS NUMEROS ES: {numero1 / numero2}')
        elif opcion = "A":
            print("SALIR DEL PROGRAMA")
            break
        else:
            if opcion != "SRMDA"
            print ("OPCION INVALIDA")
            

