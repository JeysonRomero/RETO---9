def calcular_cantidad_carne_avicola(*args):
    peso_avicola = [6, 7, 1]  
    total_carne_avicola = sum(arg * peso for arg, peso in zip(args, peso_avicola))
    
    return total_carne_avicola

cantidad_carne_avicola = calcular_cantidad_carne_avicola(*(int(input(f"Ingrese el número de {'gallinas' if i == 0 else 'gallos' if i == 1 else 'pollitos'}: ")) for i in range(3)))
print("La cantidad total de carne de aves es:", cantidad_carne_avicola, "kilogramos")
