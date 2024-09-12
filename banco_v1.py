menu = """
Escolha uma das opções abaixo
[D] - Depósito
[S] - Saque
[E] - Extrato
[Q] - Sair

"""

LIMITE = 500
LIMITE_SAQUES = 3
dep = 0
cont_dep = 1
extrato = []
valor_conta = 0
aux_saque = 0

while True:
    op = input(menu)

    if op.upper() == "D":
        print("Você escolheu a operação de depósito!\n")
        dep = int(input("Digite um valor acima de 0 reais: "))

        if dep > 0:
            extrato.append("Depósito {} -> R$ {:.2f}".format(cont_dep, dep))
            valor_conta += dep
            cont_dep += 1

    
    elif op.upper() == "S":
        print("Você escolheu a operação de saque!\n")
        valor = 0
        op_saque = "S"

        while True:
            if valor_conta == 0 or valor_conta - valor < 0:
                print("Não é possível realizar o saque pois você não tem saldo ou seu saldo ficará negativo após a operação")
                break

            if op_saque == "n".upper():
                break

            elif aux_saque == 500:
                print("Você excedeu o limite diário de saque.")
                break

            valor = int(input("Quanto você deseja sacar?\n"))
         
            if valor_conta - valor >= 0:
                valor_conta -= valor
                aux_saque += valor
            
            else:
                print("Não foi possível realizar a operação pois seu saldo ficará negativo.")
                break

            if valor >= 1 and valor <= LIMITE and valor_conta > 0:
                extrato.append("Saque {} -> R$ {:.2f}".format((LIMITE_SAQUES * - 1) +4, valor))
                LIMITE_SAQUES -= 1
                
                print(f"Novo valor em conta: R$ {valor_conta:.2f}")

                if LIMITE_SAQUES == 0 or aux_saque == 500:
                    break
                
                op_saque = input(f"Você ainda tem {LIMITE_SAQUES} saque(s) restante(s). Deseja continuar sacando [S][N]?\n").upper()
            
            elif valor_conta < valor:
                print(f"Atualmente o você tem R$ {valor_conta:.2f} na conta e por isso não é possível realizar a operação de saque.")
                break

            elif valor <= 0 or valor > LIMITE:
                print("Digite um valor correto para o saque.")
        
    
    elif op.upper() == "E":
        print("Você escolheu a operação de extrato! Segue abaixo as suas operações:\n")
        if len(extrato) == 0:
            print("Não foram realizdadas movimentações")
        else:
            for i in extrato:
                print(i)
            print(f"Saldo total: R$ {valor_conta:.2f}")

    elif op.upper() == "Q":
        print("Obrigado por usar o nosso sistema!\n")
        break
    else:
        print("Operação inválida, digite uma opção válida do menu.")
