from calculator import division, multiplicacion, resta, suma


def healthcheck():
    """Muestra el estado básico de la aplicación."""
    print("\n=================================")
    print("           HEALTHCHECK")
    print("=================================")
    print("Estado: OK")
    print("Aplicación: Calculadora DevOps")


def solicitar_numeros():
    """Solicita dos números al usuario."""
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("\nError: debe ingresar números válidos.")
        return None


def main():
    while True:
        print("\n=================================")
        print("       CALCULADORA DEVOPS")
        print("=================================")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Healthcheck")
        print("6. Salir")
        print("=================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            healthcheck()
            continue

        if opcion == "6":
            print("\n¡Hasta luego!")
            break

        if opcion not in {"1", "2", "3", "4"}:
            print("\nOpción no válida.")
            continue

        numeros = solicitar_numeros()

        if numeros is None:
            continue

        a, b = numeros

        if opcion == "1":
            resultado = suma(a, b)
        elif opcion == "2":
            resultado = resta(a, b)
        elif opcion == "3":
            resultado = multiplicacion(a, b)
        else:
            try:
                resultado = division(a, b)
            except ValueError as error:
                print(f"\nError: {error}")
                continue

        print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()
