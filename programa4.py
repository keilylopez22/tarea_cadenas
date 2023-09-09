

def numeroTelefonico():
    NumEnPartes = numero.split('-')
    NumeroSolito = NumEnPartes[1]
    return NumeroSolito

def main():
    telefono = input("ingresa tu numero telefonico (+34-...-..): ")
    if not telefono.startswith('+34-') or len(telefono ) != 16 or telefono[13] != '-':
        print("el formato del numero que ingresaste no es valido")
        return


    NumeroSolito = numeroTelefonico(telefono)
    print(f"El numero telefonico sin el prefijo y sin extension es: {NumeroSolito}")

if __name__ == "__main__":
    main()
