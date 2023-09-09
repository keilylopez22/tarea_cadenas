def obtenerPrecioEnCentimos():
    precio = float(input("ingresa el precio del producto en euros con dos decimales: "))
    euro = int(precio)
    centimo = int((precio - euro)* 100)
    return euro, centimo
euro, centimo = obtenerPrecioEnCentimos()
print(f"el precio que introdujiste es: {euro} euros y {centimo} centecimos")