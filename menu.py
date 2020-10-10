import os

def Numeros():
    print("*****Opcion de Numeros*****")
    #ingresar n numeros, donde n es un numero ingresado por tecaldo, calcular y mostrar:
    #cantidad de numeros positivos, negativos e iguales a cero.
    veces= int(input("Cuantos números desea ingresar?: "))
    pos=0
    neg=0
    cero=0
    for x in range(veces): 
        nume=int(input("Ingrese un número: "))
        if (nume>0):
            pos=pos+1
        elif(nume<0):
            neg=neg+1
        else:
            cero=cero+1
    print("Cantidad de números positivos: " + str(pos)+ 
          "\n Cantidad de números negativos : "+ str(neg)+ 
          "\n Cantidad de números iguales a cero: " + str(cero))  


    pausa=input("Presiones una tecla para continuar")

def Datos():
    print("*****Opcion de Datos de Personas*****")

    pausa=input("Presiones una tecla para continuar")


seguir=True
while (seguir):
    os.system('cls')
    print("1. Opcion Numeros" )
    Print("2. Opcion Datos de Personas ")
    print("3. Finalizar ")
    op=int(input("Ingresar opcion 1,2,3: "))
    if (op==1):
        Numeros()
    if (op==2):
        Datos()
    if (op==3):
        seguir=False
        break
