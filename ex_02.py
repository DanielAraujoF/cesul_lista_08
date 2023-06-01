# 2) Desenvolva uma função que receba dois números inteiros e retorne o maior entre eles.

def achar_maior(x: int, y: int):
    if x >= y:
        return x

    return y


primNum = int(input("Informe um número: "))
secNum = int(input("Informe um número: "))

maior = achar_maior(primNum, secNum)

print(f"O maior número é {maior}")
