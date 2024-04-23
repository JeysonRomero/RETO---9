def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)


base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")
