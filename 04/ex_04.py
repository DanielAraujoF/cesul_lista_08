# 4) Desenvolva uma função que receba o raio de uma esfera, calcule e mostre o seu volume,
# através da função:      Vol = 4/3 ∗ r²

from ex_04_funcao import calcular_volume_esfera

raio = int(input("Insira o raio da esfera: "))
volume = calcular_volume_esfera(raio)
print(f"O volume da esfera é {volume:.2f}")