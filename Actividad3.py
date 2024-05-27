NombresLista=[]

while True:
    Nombre=input("Ingrese el Nombre\n")
    NombresLista.append(Nombre)
    decision = input("Desea agregar mas Nombres S/N\n")
    if decision.lower() == "no":
        break

print(f"El Nombre mas corto antes de eliminar ",NombresLista)

if NombresLista:    
    NombreCorto = NombresLista[0]
    for Nombre in NombresLista:
        if len(Nombre) < len(NombreCorto):
            NombreCorto = Nombre
    NombresLista.remove(NombreCorto)
print(NombresLista)