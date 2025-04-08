from abc import ABC, abstractmethod
from datetime import datetime

menu = """


[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[0] Sair

=> """

usuarios = []
contas = []

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def __str__(self):
        if not self.transacoes:
            return "Nenhuma transação registrada."
        
        linhas = [
            f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}"
            for t in self.transacoes
        ]
        return "\n".join(linhas)

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def cpf(self):
        return self._cpf
    
    def __str__(self):
        return f"{self._nome} (CPF: {self._cpf})"

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        elif valor > self._saldo:
            print("Saldo insuficiente.")
            return False
        self._saldo -= valor
        return True
    
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        
        self._saldo += valor
        return True
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    def __str__(self):
        return f"Agência: {self.agencia} | Conta: {self.numero} | Titular: {self.cliente}"
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        saques_realizados = len([
            t for t in self.historico.transacoes if t["tipo"] == "Saque"
        ])
        if saques_realizados >= self._limite_saques:
            print("Limite de saques atingido.")
            return False
        elif valor > self._limite:
            print("Valor excede o limite por saque.")
            return False
        
        return super().sacar(valor)
    
    def __str__(self):
        return f"Agência: {self.agencia} | Conta: {self.numero} | Titular: {self.cliente.nome}"

def visualizar_extrato (conta):
    print("\n========= Extrato ===========")
    transacoes = conta.historico.transacoes
    
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in transacoes:
            print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("==============================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    # Verificar se CPF já existe
    usuario_existente = next((u for u in usuarios if u.cpf == cpf), None)
    if usuario_existente:
        print("Usuário já cadastrado com esse CPF.")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa):")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    novo_usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    
    print("Usuário cadastrado com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print(conta)

def cadastrar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if not usuario:
        print("Usuário não encontrado. Conta não criada.")
        return
    
    nova_conta = ContaCorrente(numero=numero_conta, cliente=usuario)
    contas.append(nova_conta)
    usuario.adicionar_conta(nova_conta)

    print("Conta criada com sucesso!")

def buscar_cliente(cpf, usuarios):
    return next((u for u in usuarios if u.cpf == cpf), None)

def buscar_conta(cliente):
    if not cliente.contas:
        print("Cliente não possui contas.")
        return None
    
    if len(cliente.contas) == 1:
        return cliente.contas[0]
    
    print("\n=== Contas Disponíveis ===")
    for i, conta in enumerate(cliente.contas, start=1):
        print(f"[{i}] Agência: {conta.agencia} | Número: {conta.numero}")

    try:
        escolha = int(input("Escolha o número da conta: "))
        return cliente.contas[escolha -1]
    except (ValueError, IndexError):
        print("Seleção inválida.")
        return None

def executar_menu():
    while True:
        opcao = input(menu)
        
        if opcao == "1":
            cpf = input("Informe o CPF do cliente:")
            cliente = buscar_cliente(cpf, usuarios)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            
            conta = buscar_conta(cliente)
            if not conta:
                continue

            try:
                valor = float(input("Digite o valor do depósito: "))
            except ValueError:
                print("Valor inválido! Digite um número válido.")
                continue
            transacao = Deposito(valor)
            cliente.realizar_transacao(conta, transacao)
            

        elif opcao == "2":
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf, usuarios)
            if not cliente:
                print("Cliente não encontrado.")
                continue

            conta = buscar_conta(cliente)
            if not conta:
                continue
            
            try:
                valor = float(input("Digite o valor do saque: "))
            except ValueError:
                print("Valor inválido! Digite um número válido.")
                continue
            transacao = Saque(valor)
            cliente.realizar_transacao(conta, transacao)

        elif opcao == "3":
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf, usuarios)
            if not cliente:
                print("Cliente não encontrado.")
                continue

            conta = buscar_conta(cliente)
            if not conta:
                continue

            visualizar_extrato(conta)

        elif opcao == "4":
            cadastrar_usuario(usuarios)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            cadastrar_conta("0001", numero_conta, usuarios, contas)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            break
        else:
            print("Operação inválida. Tente novamente.")

executar_menu()