
def correoElectronico(correo):
    nombre, dominio = correo.split('@')
    nuevoCorreo = nombre + '@ceu.es'
    return nuevoCorreo

def main():
    correo = input("ingrese su correo electronico: ")
     
    if '@' not in correo:
        print("el correo introducido no es valido")
        return

    nuevoCorreo = correoElectronico(correo)
    print(f"tu nuevo correo con dominio ceu.es es: {nuevoCorreo}")

if __name__ == "__main__":
    main()
