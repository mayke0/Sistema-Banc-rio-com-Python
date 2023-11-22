menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: {valor:.2f}\n'
            numero_saques += 1

        else:
            print('limite de saques atingido')

    elif opcao == "3":
        print(f'------Extrato:------\n')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'Saldo : R$ {saldo:.2f}')

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")