from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('\n-----------------------------------------------\n'
          '-------------------- ATM ----------------------\n'
          '----------------- Geek Bank ------------------\n'
          'Selecione uma opção do menu:\n'
          '1 - Criar conta\n'
          '2 - Efetuar saque\n'
          '3 - Efetuar depósito\n'
          '4 - Efetuar transferência\n'
          '5 - Listar contas\n'
          '6 - Sair do sistema\n')

    op: int = int(input('Opção: '))

    if op == 1:
        criar_conta()
    elif op == 2:
        efetuar_saque()
    elif op == 3:
        efetuar_deposito()
    elif op == 4:
        efetuar_transferencia()
    elif op == 5:
        listar_contas()
    elif op == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Escolha uma opção válida!')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('\nInforme os dados do cliente')
    nome: str = input('Nome: ')
    email: str = input('Email: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data de nascimento: ')
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)
    contas.append(conta)

    print(f'Conta criada com sucesso!\n'
          f'-------------------------\n'
          f'{conta}')
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta que deseja acessar: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: R$'))
            conta.sacar(valor)
            menu()
        else:
            print(f'Desculpe, conta {numero} não encontrada.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta que deseja acessar: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor de depósito: R$'))
            conta.depositar(valor)
            menu()
        else:
            print(f'Desculpe, conta {numero} não encontrada.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def efetuar_transferencia() -> None:
    if len(contas) == 0:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()
    elif len(contas) == 1:
        print('Não existem contas suficientes para realização de uma transferência.')
        sleep(2)
        menu()
    else:
        numero_origem: int = int(input('Informe o número da conta de origem: '))

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Informe o número da conta de destino: '))

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: R$'))
                conta_origem.transferir(conta_destino, valor)
                menu()
            else:
                print(f'Desculpe, conta {numero_destino} não encontrada.')
                sleep(2)
                efetuar_transferencia()
        else:
            print(f'Desculpe, conta {numero_origem} não encontrada.')
            sleep(2)
            menu()


def listar_contas() -> None:
    if len(contas) > 0:

        print('Listagem de contas:')
        for conta in contas:
            print(conta)
            sleep(1)
        menu()
    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.id == numero:
                c = conta

    return c


if __name__ == '__main__':
    main()
