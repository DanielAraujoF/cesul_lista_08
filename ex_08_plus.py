# def calcularFatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * calcularFatorial(n - 1)
#
#
# def calcularArranjos(n, p):
#     numerador = calcularFatorial(n)
#     denominador = calcularFatorial(n - p)
#     arranjos = numerador / denominador
#     return arranjos
#
#
# def calcularCombinacoes(n, p):
#     numerador = calcularFatorial(n)
#     denominador = calcularFatorial(p) * calcularFatorial(n - p)
#     combinacoes = numerador / denominador
#     return combinacoes


while True:
    print("1 - Calcular Combinação")
    print("2 - Calcular Arranjo")
    print("3 - Sair")

    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        n = int(input("Digite o valor de n: "))
        p = int(input("Digite o valor de p: "))
        combinacoes = calcularCombinacoes(n, p)
        print("O valor das combinações é:", combinacoes)
    elif opcao == 2:
        n = int(input("Digite o valor de n: "))
        p = int(input("Digite o valor de p: "))
        arranjos = calcularArranjos(n, p)
        print("O valor dos arranjos é:", arranjos)
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")
