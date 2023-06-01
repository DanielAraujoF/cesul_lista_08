# 1) Desenvolva uma função que receba um número inteiro e retorne como saída o valor absoluto deste número.

# se entrar no if, o fluxo encontra o "return x * -1" e acaba ali mesmo a função e não chega no "return x".
def obt_val_absol(x: int) -> int:
    if x < 0:
        return x * -1
    return x


numEx = int(input("Informe um número: "))

absoluto = obt_val_absol(numEx)

print(f"O valor absoluto de {numEx} é {absoluto}")