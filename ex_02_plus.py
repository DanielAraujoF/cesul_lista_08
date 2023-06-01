# 2) Desenvolva uma função que receba dois números inteiros e retorne o maior entre eles.

# mesmo que fique mais confuso, é apenas uma possibilidade
def achar_maior(x: int, y: int) -> int:
    return x if x >= y else y


primNum = int(input("Informe um número: "))
secNum = int(input("Informe um número: "))

maior = achar_maior(primNum, secNum)

print(f"O maior número é {maior}")
