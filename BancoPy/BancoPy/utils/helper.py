from datetime import date, datetime


def data_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_data(data: str) -> date:
    return datetime.strftime(data, '%d/%m/%Y')


def formata_float_para_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'

    C:\Users\Roberto\Documents\GitHub\BancoPy\BancoPy