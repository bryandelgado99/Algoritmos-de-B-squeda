#Algoritmo de Busqueda Lineal
def imprimir_array(arreglo):
  tamanio = len(arreglo)
  for i in range(tamanio):
    print(f'[{arreglo[i]}]',end="")

def alg_busqueda_lineal(arreglo,suedlo):
  resultado = False
  tamanio = len(arreglo)

  for i in range(tamanio):
    if (arreglo[i] == sueldo):
      resultado = True
      return resultado
  return resultado

lista_sueldo = [20, 29.8, 156, 45, 1249, 24.56, 565.33, 65.6, 200]
imprimir_array(lista_sueldo)

sueldo = float(input("\n\nIngrese el sueldo a buscar: "))
respuesta = alg_busqueda_lineal(lista_sueldo, sueldo)

if respuesta:
  print("\nEl sueldo fue encontrado en el sistema")
else:
  print("\nNo existe el sueldo en el sistema")