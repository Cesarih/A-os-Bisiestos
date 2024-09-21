# Este programa sirve para calcular el número de años bisiestos entre 1900 y un año dado

# Solicitamos al usuario que ingrese un año entre 1900 y 2199
while True:
    año_ingresado = int(input("Ingrese un año entre 1900 y 2199: "))
    if 1900 <= año_ingresado <= 2199:
        break
    else:
        print("Año fuera de rango. Intente nuevamente.")

# Inicializamos la variable que almacenará la cantidad de años bisiestos
cantidad_bisiestos = 0

# Iteramos desde 1900 hasta el año ingresado
for año in range(1900, año_ingresado + 1):
    # Verificamos si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        cantidad_bisiestos += 1

# Mostramos la cantidad de años bisiestos
print(f"Entre 1900 y {año_ingresado} hay {cantidad_bisiestos} años bisiestos.")