nombres = []
for i in range(3):
    largo = input(f"ingrese el nombre {i + 1}: ")
    len(largo)
    print(f"el largo de {largo} es: {len(largo)}")
    nombres.append(largo)
nombrelargo = max(nombres, key=len)
print("El nombre mas largo es:",nombrelargo)
