sestaBasica = input("ingresa los productos de tu sesta separados por comas: ")

productos = sestaBasica.split(',')
for producto in productos:
   print(producto.strip())   
