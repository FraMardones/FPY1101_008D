saldo = int(120000)
continuar = 1
while continuar != 2:
    while True:
        try:
            opc = int(input("bienvenido, \n1.retirar\n2.depositar\nelija"))
            break
        except ValueError:
            print("valor invalido")
    if opc == 1:
        retiro = int(input("cuanto dinero quiere retirar? "))
        if retiro <= saldo:
            total = saldo - retiro
            print(f"retiro completado correctamente, saldo restante {total}")
        elif retiro > saldo:
            print("Saldo insuficiente")
            break
        continuar = int(input("desea hacer otra operacion? si(1)/no(2)"))
        if continuar == 1:
            saldo = saldo - retiro
        elif continuar == 2:
            print("nos vemos")
    elif opc == 2:
        deposito = int(input("cuanto dinero quiere depositar? "))
        total = saldo + deposito
        print(f"deposito completado correctamente, saldo restante {total}")
        continuar = int(input("desea hacer otra operacion? si(1)/no(2)"))
        if continuar == 1:
            saldo = saldo + deposito
        elif continuar == 2:
            print("nos vemos")
