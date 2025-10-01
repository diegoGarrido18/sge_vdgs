n = int(input("Introduce un número: "))

factorial = 1

if ( n < factorial):
    print("No se puede calcular el factorial de un número negativo")
else:
    for i in range(1, n + 1):
        factorial *= i

print(f"El factorial de {n} es {factorial}")
