# 1) Desenvolva uma função que receba um número inteiro e retorne como saída o valor absoluto deste número.

def obt_val_absol(x: int) -> int:
    if x < 0:
        val_absol = x * -1
    else:
        val_absol = x

    return val_absol


numEx = int(input("Informe um número: "))

absoluto = obt_val_absol(numEx)

print(f"O valor absoluto de {numEx} é {absoluto}")