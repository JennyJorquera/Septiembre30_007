#crear ciclo for que permita ingresar n temperatura donde n es un numero ingresado por teclado
#mostrar cuantas temperaturas estan por sobre 0 y cuantas temperaturas estan bajo o igual a 0
sobrecero=0
bajocero=0
veces=int(input("Cuantas temperaturas quiere ingresar?: "))
for i in range(veces):
    tempe=float(input("Ingrese temperatura: "))
    if (tempe>0):
        sobrecero=cobrecero+1
    else:
        bajocero=bajocero+1
#mostrar datos
print("La cantidad de temperaturas mayores a 0 es: " + str(sobrecero))
print("La cantidad de temperaturas menor o igual a cero e: " + str(bajocero))

