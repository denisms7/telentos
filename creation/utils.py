import re


def clean_cpf(cpf: str) -> str:
    if not cpf:
        return cpf

    return re.sub(r'\D', '', str(cpf))


def is_valid_cpf(cpf: str) -> bool:
    cpf = clean_cpf(cpf)

    if not cpf or len(cpf) != 11:
        return False

    # Bloqueia CPFs com todos os dígitos iguais
    if cpf == cpf[0] * 11:
        return False

    soma_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig_1 = (soma_1 * 10 % 11) % 10

    soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig_2 = (soma_2 * 10 % 11) % 10

    return (int(cpf[9]) == dig_1 and int(cpf[10]) == dig_2)
