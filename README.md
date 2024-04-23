# RETO---9

<br>
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_9 en slack

<br>

## 1.De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

<br>

#### PUNTO 1 - (RETO 7) Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.


<br>

```py
imprimir_cuadrados = (lambda: [print(f"Número: {num}, Cuadrado: {num ** 2}") for num in range(1, 101)])()
```
<br>

#### PUNTO 2 - (RETO 7) -Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

<br>

```py
imprimir_impares = (lambda: [print(i) for i in range(1, 1000, 2)])()

imprimir_pares = (lambda: [print(i) for i in range(2, 1001, 2)])()

```
<br>

#### PUNTO 3 - (RETO 7) -Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado


<br>

```py
imprimir_pares_descendentes = (lambda n: (
    lambda: (
        print(f"Números pares descendentes hasta 2 para n={n}:"),
        [print(i) for i in range(n, 1, -2)]
    )() if n >= 2 else print("El número ingresado no es válido. Por favor, ingrese un número natural mayor o igual a 2.")
))(int(input("Ingrese un número natural mayor o igual a 2: ")))

```
<br>

## 2.De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

#### PUNTO 3 - (RETO 6)- Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.


<br>

```py
def calcular_cantidad_carne_avicola(*args):
    peso_avicola = [6, 7, 1] 
    total_carne_avicola = sum(arg * peso for arg, peso in zip(args, peso_avicola))
    
    return total_carne_avicola

cantidad_carne_avicola = calcular_cantidad_carne_avicola(*(int(input(f"Ingrese el número de {'gallinas' if i == 0 else 'gallos' if i == 1 else 'pollitos'}: ")) for i in range(3)))
print("La cantidad total de carne de aves es:", cantidad_carne_avicola, "kilogramos")


```
<br>

#### PUNTO 4 - (RETO 6) -Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

<br>

```py
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


```
<br>

#### PUNTO 5 - (RETO 6) -Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

<br>

```py
calcular_valor_prestamo = lambda C, i, n: C * (1 + i / 100) ** n

C, i, n = [float(input("Ingrese el monto del préstamo: ")), 
           float(input("Ingrese la tasa de interés anual (%): ")), 
           int(input("Ingrese el número de meses: "))]

valor_prestamo = calcular_valor_prestamo(C, i, n)

print("El valor del préstamo después de", n, "meses es:", valor_prestamo)


```
<br>

## 3.Escriba una función recursiva para calcular la operación de la potencia.

<br>

```py

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

```
<br>


## 4. Utilice la siguiente plantilla de code para contar el tiempo:

<br>

```py

import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
<br>

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.


<br>

### Funcion iterativa

<br>

```py

import time

def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

limite_superior = 35  # Define el límite superior para calcular la serie Fibonacci

start_time = time.time()
fib_iterativo = fibonacci_iterativo(limite_superior)
end_time = time.time()

print(f"Fibonacci iterativo para n={limite_superior}: {fib_iterativo}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

```
<br>

### Funcion recursiva

<br>

```py
import time

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

limite_superior = 35  # Define el límite superior para calcular la serie Fibonacci

start_time = time.time()
fib_recursivo = fibonacci_recursivo(limite_superior)
end_time = time.time()

print(f"Fibonacci recursivo para n={limite_superior}: {fib_recursivo}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

```
<br>

Este código prueba los valores de la serie Fibonacci desde 35 hasta 44. Calcula el tiempo de ejecución para ambas implementaciones (recursiva e iterativa) y muestra la diferencia de tiempo. Podemos observar en qué punto la diferencia de tiempo comienza a ser significativa.

<br>

## 5.Crear cuenta en stackoverflow y adjuntar imagen en el repo
