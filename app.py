menu = """


[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

def realizar_deposito(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R${valor:.2f} foi realizado com sucesso")
    else:
        print("Valor inserido é inválido.")
    return saldo, extrato

def realizar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print(f"Valor excede o limite de R${limite:.2f} por saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:     R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"O saque de R${valor:.2f} foi realizado com sucesso")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, numero_saques

def visualizar_extrato (saldo, /, *, extrato):
    print("\n========= Extrato ===========")
    print(" Não foram realizadas movimentações." if not extrato else f"\n{extrato}")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    # Verificar se CPF já existe
    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario_existente:
        print("Usuário já cadastrado com esse CPF.")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa):")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Conta: {conta['numero']}")
        print(f"Titular: {conta['usuario']['nome']}")

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado. Conta não criada.")
        return
    
    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario
    }

    contas.append(conta)
    print("Conta criada com sucesso!")

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        saldo, extrato = realizar_deposito(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        saldo, extrato, numero_saques = realizar_saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )
    elif opcao == "3":
        visualizar_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        cadastrar_usuario(usuarios)
    elif opcao == "5":
        numero_conta = len(contas) + 1
        cadastrar_conta("0001", numero_conta, usuarios)
    elif opcao == "6":
        listar_contas(contas)
    elif opcao == "0":
        break
    else:
        print("Operação inválida. Tente novamente.")