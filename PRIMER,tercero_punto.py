imprimir_pares_descendentes = (lambda n: (
    lambda: (
        print(f"Números pares descendentes hasta 2 para n={n}:"),
        [print(i) for i in range(n, 1, -2)]
    )() if n >= 2 else print("El número ingresado no es válido. Por favor, ingrese un número natural mayor o igual a 2.")
))(int(input("Ingrese un número natural mayor o igual a 2: ")))
