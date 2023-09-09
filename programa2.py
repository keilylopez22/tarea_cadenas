nombreCompleto = input("escribe tu nombre completo: ")
nombre_en_mayusculas = nombreCompleto.upper()
nombre_en_minusculas = nombreCompleto.lower()
nombredividido = nombreCompleto.split()
nombreCapitalizado= ' '.join([parte.capitalize() for parte in nombredividido])
print(nombre_en_minusculas)
print(nombre_en_mayusculas)
print(nombreCapitalizado)







