# Crear un arreglo de 3x3x3 manualmente con los valores especificados
arreglo = [
    [["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"]],
    [["Blanco", "amarillo", "rojo"], ["Naranja", "Verde", "Blanco"], ["amarillo", "rojo", "Naranja"]],
    [["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"], ["Blanco", "amarillo", "rojo"]]
]

# Inicializar contadores para cada color
contador_amarillo = 0
contador_rojo = 0
contador_Naranja = 0
contador_Verde = 0
contador_Blanco = 0

# Contar los elementos de cada color en el arreglo
for i in range(3):
    for j in range(3):
        for k in range(3):
            if arreglo[i][j][k] == "amarillo":
                contador_amarillo += 1
            elif arreglo[i][j][k] == "rojo":
                contador_rojo += 1
            elif arreglo[i][j][k] == "Naranja":
                contador_Naranja += 1
            elif arreglo[i][j][k] == "Verde":
                contador_Verde += 1
            elif arreglo[i][j][k] == "Blanco":
                contador_Blanco += 1

# Mostrar la información
print(f"Número de elementos 'amarillo': {contador_amarillo}")
print(f"Número de elementos 'rojo': {contador_rojo}")
print(f"Número de elementos 'Naranja': {contador_Naranja}")
print(f"Número de elementos 'Verde': {contador_Verde}")
print(f"Número de elementos 'Blanco': {contador_Blanco}")

