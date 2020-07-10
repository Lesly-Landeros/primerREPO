#escribe un programa que pida al usuario un texto y un numero entero
#mandar a imprimir en pantalla el texto repetido las veces indicado por el numero 
#el  numero NOTA: HACER EL PROGRAMA USANDO UNA FUNCION 
#
#INGRESA UN TEXTO: HOLA
#INGRESA UN NUMERO:4
#SALIDA:
#HOLA
#HOLA
#HOLA
#HOLA

#DECLARAR LA FUNCION 

def repetir(texto, numero):
    texto += '\n'
    print (texto*numer)

#escribir el codigo
T= input("ingresa un texto ")
N= int(input("ingresa un numero "))

repetir(T,N)
