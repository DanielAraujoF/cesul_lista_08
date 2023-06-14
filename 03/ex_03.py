# 3) Desenvolva uma função que receba um número inteiro e positivo N e retorne a soma dos N
#    números inteiros existentes entre o número 1 e esse número

def soma(x: int):
    if x == 1:
        return 1
    else:
        return x + soma(x - 1)


numero = int(input("Insira um número: "))

calculo = soma(numero)
print(calculo)
