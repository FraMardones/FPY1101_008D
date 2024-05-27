matriz = []
lista = []
for i in range(3):
    lista = [input(f"ingrese el digito {j + 1} ({i + 1}): ") for j in range(4)]
    matriz.append(lista)
print(matriz)