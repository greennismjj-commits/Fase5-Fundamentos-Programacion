# Universidad Nacional Abierta y a Distancia - UNAD
# Programa: Ingeniería Electrónica
# Curso: Fundamentos de Programación
# Código del curso: 213022
# Fase 5 - Evaluación Final POA
# Problema 3: Reabastecimiento de inventario
# Estudiante: Aura Maria Brito Rodriguez
# Grupo: 213022_131
# Tutor: Javier Mauricio López Moreno

# Matriz con los datos de los cinco artículos
inventario = [
    ["A001", "Martillos", 5, 15],
    ["A002", "Destornilladores", 20, 10],
    ["A003", "Alicates", 3, 12],
    ["A004", "Llaves inglesas", 10, 10],
    ["A005", "Cintas métricas", 4, 15]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Presentación del encabezado
print("INFORME DE REABASTECIMIENTO DE INVENTARIO")
print("-" * 48)
print(f'{"Artículo":25} {"Cantidad a pedir":>18}')

# Recorro la matriz para evaluar cada artículo
for articulo in inventario:
    nombre = articulo[1]
    cantidad = calcular_pedido(articulo[2], articulo[3])

    # Muestro el resultado de cada artículo
    print(f"{nombre:25} {cantidad:18d}")
