frase = input("ingresa una frase: ")
vocal = input("ingrese una vocal: ")
salida = " "
for letra in frase:
    if letra == vocal:
        salida += letra.upper()
    else:
        salida += letra
print(salida)            

