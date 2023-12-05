# Definir la función de la esquina noroeste
def esquina_noroeste(derecha, abajo, costo):
    
  # Verificar si la oferta y la demanda son iguales
  if sum(derecha) != sum(abajo):
    # Si la oferta es mayor que la demanda, agregar una demanda ficticia
    if sum(derecha) > sum(abajo):
      abajo.append(sum(derecha) - sum(abajo))
      for i in range(len(costo)):
        costo[i].append(0)  # Agregar el costo ficticio a todas las filas
    # Si la demanda es mayor que la oferta, agregar una oferta ficticia
    else:
      derecha.append(sum(abajo) - sum(derecha))  # Aquí está la corrección
  
  # Inicializar la solución con ceros
  solucion = [[0 for j in range(len(abajo))] for i in range(len(derecha))]
  # Iniciar en la celda de la esquina noroeste
  i = 0
  j = 0

  # Iterar hasta asignar todas las unidades posibles
  while i < len(derecha) and j < len(abajo):
    
    # Asignar la cantidad mínima entre total derecha y total abajo disponibles
    asignacion = min(derecha[i], abajo[j])
    solucion[i][j] = asignacion
    # Actualizar total derecha y total abajo restantes
    derecha[i] -= asignacion
    abajo[j] -= asignacion
    
    # Eliminar la fila o la columna que se haya agotado
    if derecha[i] == 0:
      i += 1
    elif abajo[j] == 0:
      j += 1
    
  # Retornar la solución y el costo total
  costoTotal = sum(costo[i][j] * solucion[i][j] for i in range(len(derecha)) for j in range(len(abajo)))
  return solucion, costoTotal

# Le pide al usuario que ingrese los datos del problema
print("\n \n \nIngresa el total de la derecha (separado por espacios) (ej. 300 200 300 100):")
derecha = list(map(int, input().split()))
print("Ingresa el total de abajo (separado por espacios) (ej. 200 200 300 100 100 ):")
abajo = list(map(int, input().split()))
print("Ingresa los costos de cada fila (separada por espacios, da ENTER para pasar a la próxima fila: (ej. 2 3 4 5 6 (enter) )")
costo = [list(map(int, input().split())) for i in range(len(derecha))]

# Mostrar la suma de los totales
print("\n \nLa suma del total de la derecha es:")
sumaTotalDerecha = sum(derecha)
print(sumaTotalDerecha)

print("La suma del total de abajo es:")
sumaTotalAbajo = sum(abajo)
print(sumaTotalAbajo)

diferenciaTotal = sumaTotalDerecha - sumaTotalAbajo
print("\nLa diferencia de los totales es: ", diferenciaTotal)


# Se llama a la función con los datos que fueron ingresados
solucion, costoTotal = esquina_noroeste(derecha, abajo, costo)

# Mostrar la solución
print("La solución óptima es:\n")
for fila in solucion:
  print(fila)
print(f"\nEl costo total es: {costoTotal}")