año_inicio = 1900
año_final = 2199

def es_bisiesto(año):
  if año % 4 == 0:
    if año % 100 == 0:
      if año % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def contar_bisiestos(año_final):
  bisiestos = 0
  for año in range(año_inicio, año_final + 1):
    if es_bisiesto(año):
      bisiestos += 1
  return bisiestos

año_entrada = int(input("Ingrese un año entre 1900 y 2199: "))

if año_entrada >= año_inicio and año_entrada <= año_final:
  bisiestos = contar_bisiestos(año_entrada)
  print(f"Hay {bisiestos} años bisiestos entre {año_inicio} y {año_entrada}.")
else:
  print("El año ingresado no está dentro del rango permitido.")