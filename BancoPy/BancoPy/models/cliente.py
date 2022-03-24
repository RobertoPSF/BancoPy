from datetime import date
from utils.helper import data_para_str, str_para_data


class Cliente:
    contador: int = 1

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__id: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_data(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return data_para_str(self.__data_nascimento)

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def data_cadastro(self: object) -> str:
        return data_para_str(self.__data_cadastro)

    def __str__(self: object):
        return f'Código: {self.id}\nNome: {self.nome}\nData de nascimento: {self.data_nascimento}\n' \
               f'Data cadastro: {self.data_cadastro}\n\n'

