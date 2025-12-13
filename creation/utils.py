import re


def is_valid_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf in (c * 11 for c in '0123456789'):
        return False

    soma_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig_1 = (soma_1 * 10 % 11) % 10

    soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig_2 = (soma_2 * 10 % 11) % 10

    return (
        int(cpf[9]) == dig_1
        and int(cpf[10]) == dig_2
    )
