menu = """======== [1] Depositar ======== 
          ======== [2] Sacar ======== 
          ======== [3] Extrato ======== 
          ========  [4] nada ========  
       """

saldo = 50
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input(f"Qual o valor do deposito? "))
        if deposito > 1:
            saldo += deposito
            print(f"Seu saldo é de {saldo}")
        else:
            print("Digite um valor váli do")

    elif opcao == 2:
        saque = int(input("Qual valor deseja sacar? "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite = saque > limite
        excedeu_saldo = saque > saldo
        if saldo > saque:
            saldo -= saque
            print(f"saque realizado com sucesso, seu saldo é de {saldo - saque}")
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1

        elif excedeu_limite:
            print("O limite de saque é 500.")

        elif excedeu_saques:
            print("Atingiu o numero maximo de saques")

        elif excedeu_saldo:
            print("saldo insuficiente")

    elif opcao == 3:
        print("===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"saldo: R$ {saldo:.2f}")

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
