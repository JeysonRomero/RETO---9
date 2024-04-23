calcular_valor_prestamo = lambda C, i, n: C * (1 + i / 100) ** n

C, i, n = [float(input("Ingrese el monto del préstamo: ")), 
           float(input("Ingrese la tasa de interés anual (%): ")), 
           int(input("Ingrese el número de meses: "))]

valor_prestamo = calcular_valor_prestamo(C, i, n)

print("El valor del préstamo después de", n, "meses es:", valor_prestamo)
