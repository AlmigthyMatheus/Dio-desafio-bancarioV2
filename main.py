menu = """
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
[u] Criar Usuário
[c] Criar Conta Corrente

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_conta = 1


def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nValor depositado: R$ {valor:.2f}"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor <= saldo and valor <= limite:
            saldo -= valor
            numero_saques += 1
            extrato += f"\nValor sacado: R$ {valor:.2f}"
            print("Saque efetuado com sucesso!")
        else:
            print("Saque falhou! Verifique se o valor está dentro do limite e se há saldo suficiente.")
    else:
        print("Número máximo de saques atingido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, *, extrato):
    print("\nExtrato:")
    print("Nenhuma transação realizada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")


def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário já está cadastrado.")
            return

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")


def criar_conta_corrente(cpf):
    global numero_conta
    AGENCIA = "0001"

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
            contas.append(conta)
            print(f"Conta corrente criada com sucesso! Agência: {AGENCIA}, Conta: {numero_conta}")
            numero_conta += 1
            return

    print("CPF não encontrado. Crie um usuário primeiro.")


def listar_contas():
    if not contas:
        print("Nenhuma conta foi criada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Insira o valor que deseja sacar: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        cpf = input("CPF (apenas números): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta_corrente(cpf)

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
