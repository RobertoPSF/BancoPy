from models.cliente import Cliente
from utils.helper import formata_float_str_moeda
from time import sleep


class Conta:
    contador = 1

    def __init__(self: object, cliente: Cliente) -> None:
        self.__id: int = Conta.contador
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 1500.0
        self.__saldo_total: float = self.calcula_saldo_total
        Conta.contador += 1

    def __str__(self: object):
        return f'Número da conta: {self.id}\nCliente: {self.cliente.nome}\n' \
               f'Saldo total: {formata_float_str_moeda(self.saldo_total)}\n\n'

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self.calcula_saldo_total
            print('Depósito efetuado com sucesso!')
            sleep(2)
        else:
            print('Erro ao tentar efetuar o depósito. Tente novamente.')

    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saldo_total = self.calcula_saldo_total
            else:
                restante: float = valor - self.saldo
                self.limite -= restante
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
            print('Saque realizado com sucesso!')
            sleep(2)
        else:
            print('Saque não realizado. Tente novamente.')
            sleep(2)

    def transferir(self: object, conta_destino: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
                conta_destino.saldo = conta_destino.saldo + valor
                conta_destino.saldo_total = conta_destino.calcula_saldo_total
            else:
                restante: float = valor - self.saldo
                self.limite = self.limite - restante
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
                conta_destino.saldo = conta_destino.saldo + valor
                conta_destino.saldo_total = conta_destino.calcula_saldo_total
            print('Transferência realizada com sucesso!')
            sleep(2)
        else:
            print('Transferencia não realizada. Tente novamente.')
            sleep(2)
