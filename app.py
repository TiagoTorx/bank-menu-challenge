menu = """


[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def realizar_deposito():
    global saldo
    global extrato
    deposito = float(input("Digite o valor do depósito: "))
    
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"O valor de R${deposito:.2f} foi realizado com sucesso")
    else:
        print("Valor inserido é inválido.")

def realizar_saque():
    global saldo
    global LIMITE_SAQUES
    global limite
    global numero_saques
    global extrato
    print(f"Número de saques: {numero_saques} de {LIMITE_SAQUES}")
    valor_de_saque = float(input("Digite o valor que deseja sacar: "))

    if valor_de_saque > limite:
        print(f"Valor excede o limite de R${limite:.2f} por saque.")
    elif valor_de_saque > saldo:
        print("Saldo insuficiente.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques diários atingido.")
    elif valor_de_saque > 0:
        saldo -= valor_de_saque
        extrato += f"Saque:     R$ {valor_de_saque:.2f}\n"
        numero_saques += 1
        print(f"O saque de R${valor_de_saque:.2f} foi realizado com sucesso")
    else:
        print("Valor inválido para saque.")

def visualizar_extrato ():
    print("\n========= Extrato ===========")
    print(" Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================")

while True:

    opcao = input(menu)
    
    if opcao == "1":
        realizar_deposito()
    elif opcao == "2":
        realizar_saque()
    elif opcao == "3":
        visualizar_extrato()
    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")