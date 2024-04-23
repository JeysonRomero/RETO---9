calcular_vueltas = lambda *args: (
    lambda P, M, H, B: (
        lambda precio_pan, precio_leche, precio_huevo: (
            lambda costo_total, vueltas: vueltas if vueltas >= 0 else abs(vueltas)
        )(P * precio_pan + M * precio_leche + H * precio_huevo, B - (P * precio_pan + M * precio_leche + H * precio_huevo))
    )(*args)
)

P, M, H, B = [int(input(f"Ingrese la cantidad de {'panes' if i == 0 else 'bolsas de leche' if i == 1 else 'huevos'} a comprar: ")) for i in range(3)] + [int(input("Ingrese el valor del billete entregado: "))]

vueltas = calcular_vueltas(P, M, H, B)

print("Las vueltas son:", vueltas)
