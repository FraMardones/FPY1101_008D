NombresList=[]
ApellidosList=[]
for i in range(3):
    Nom=input("Ingrese el Nombre\n")
    NombresList.append(Nom)
    Apellido=input("Ingrese el apellido\n")
    ApellidosList.append(Apellido)
    
NombresList.sort()
ApellidosList.sort()
print(NombresList)
print(ApellidosList)    
