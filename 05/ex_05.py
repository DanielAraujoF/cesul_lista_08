# 5) Desenvolva um programa que calcule a área de uma figura geométrica de acordo com a
# opção do usuário, sendo:

# Opção | Figura Geométrica | Fórmula
#   1   |   Quadrado        | A = l2
#       |                   | Onde:
#       |                   | - l: Lado do Quadrado
# --------------------------------------------------------
#   2   |    Círculo        | A = p * r2
#       |                   | Onde
#       |                   | - p: 3.14
#       |                   | - r: Raio da Circunferência
# --------------------------------------------------------
#   3   |   Triângulo       |  A = (b * h) / 2
#       |                   |  Onde
#       |                   |  - b: Base do Triângulo
#       |                   |  - h: Altura do Triângulo
#
# O sistema deverá solicitar ao usuário qual opção deseja, e, de acordo com a opção de o
# usuário solicitar as entradas para a realização do cálculo. Exibir como saída o resultado obtido
# no cálculo

from ex_05_funcoes import area_quadrado, area_triangulo, area_circulo
# ou from ... import * (vai puxar todas as funções)

tipoFormaGeo = int(input("Qual a forma geométrica?\n 1 - Quadrado.\n 2 - Círculo\n 3 - Triângulo\n R: "))

if tipoFormaGeo == 1:
    lado = int(input("Como o cálculo de área do quadrado é lado x lado, informe o tamanho de apenas um lado do quadrado: "))
    print(area_quadrado(lado))

elif tipoFormaGeo == 2:
    raio = int(input("Insira o raio do círculo: "))
    print(area_circulo(raio))

else:
    base = int(input("Insira a base do triângulo: "))
    altura = int(input("Insira a altura do triângulo: "))
    print(area_triangulo(base, altura))
