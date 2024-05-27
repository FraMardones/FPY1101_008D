import os
import time
usuario = []
contraseña=[]
while True:
    opc = int(input("====================\nMenu\n1.Iniciar sesion\n2.Registrar usuario\n3.Eliminar Usuario\n4.Salir\n====================\nSeleccione: "))
    time.sleep(1)
    os.system("cls")
    if opc == 1:
        nombre = input("ingrese usuario: ")
        contra = input("ingrese contraseña: ")
        if nombre in usuario:
            index = usuario.index(nombre)
            if contraseña[index] == contra:
                print(f"Bienvenido {nombre}!!")
        else:
            print("Usuario o contraseña incorrecta")
        time.sleep(1)
        os.system("cls")
    elif opc == 2:
        nombre = input("Ingrese usuario: ")
        usuario.append(nombre)
        contra = input("Ingrese contraseña: ")
        contraseña.append(contra)
        print("Se ha registrado correctamente")
        time.sleep(1)
        os.system("cls")
    elif opc == 3:
        nombre = input("Ingrese el nombre del usuario que va a eliminar: ")
        contra = input("Ingrese la contraseña: ")
        if nombre in usuario:
            index = usuario.index(nombre)
            if contraseña[index] == contra:
                usuario.remove(nombre)
                contraseña.remove(contra)
            print("Usuario eliminado correctamente")
        else:
            print("Usuario o contraseña incorrecta.")
        time.sleep(1)
        os.system("cls")
    elif opc == 4:
        print("Nos vemos")
        break
    else:
        print("Valor incorrecto, ingrese otro")
    time.sleep(1)
    os.system("cls") 