


fechaDeNacimiento = input("ingresa tu fecha de nacimiento, tienes que escribirla en el siguiente formato 09/03/22: ")
dia = fechaDeNacimiento[:fechaDeNacimiento.find("/")]
mesAnio= fechaDeNacimiento[fechaDeNacimiento.find("/")+1:]

mes= mesAnio[:mesAnio.find("/")]
anio = mesAnio[mesAnio.find("/")+1:]
print("el dia de tu nacimiento es: ", dia)
print("el mes de tu nacimiento es: ", mes) 
print("el año de tu nacimiento es: ", anio)

