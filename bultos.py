masbultos = True
bultoliviano = 1000
bultonormal = 2000
cantidadbulto = 0
cantidadbulto2 = 0
print("Bienvenido")
while masbultos != 2:
    pesobulto = int(input("Ingrese peso del bulto en kg, (ejemplo: 1): "))
    if pesobulto >= 1 or pesobulto <= 5:
            print("Su bulto es liviano")
            cantidadbulto = int(input("¿Cuantos va a llevar que sean del mismo peso anterior?: "))
            break
    elif pesobulto >= 6 or pesobulto <=10:
            print("Su bulto es normal")
            cantidadbulto2 = int(input("¿Cuantos va a llevar que sean del mismo peso anterior?: "))
            break
masbultos = int(input("¿Quiere llevar mas bultos? si(1)/no(2): "))
print(f"Bultos livianos: ${1000 * cantidadbulto}")
print(f"Bultos Normales: ${2000 * cantidadbulto2}")
print(f"Total a pagar: ${(1000 * cantidadbulto) + (2000 * cantidadbulto2)} ")

