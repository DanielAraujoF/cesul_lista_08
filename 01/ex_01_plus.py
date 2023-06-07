# 1) Desenvolva uma função que receba um número inteiro e retorne como saída o valor absoluto deste número.

def obt_val_absol(x: int) -> int:
    if x < 0:
        return x * -1
    else:
        return x


numEx = int(input("Informe um número: "))

absoluto = obt_val_absol(numEx)

print(f"O valor absoluto de {numEx} é {absoluto}")

