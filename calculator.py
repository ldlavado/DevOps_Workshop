def resta(a, b):
    """Resta dos números."""
    return a - b


def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b


def suma(a, b):
    """Suma dos números."""
    return a - b


def division(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b
