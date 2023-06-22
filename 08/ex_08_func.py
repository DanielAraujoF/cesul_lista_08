def calc_fat(x: int):
    if x == 1:
        return 1
    else:
        return x * calc_fat(x - 1)


resultado = 1


def exibir_menu() -> int:
    return int(input("O que deseja fazer? \n"
                     "1 - Calcular arranjo: \n"
                     "𝐴 = 𝑛! / (𝑛 − 𝑝)! \n\n"
                     "2 - Calcular combinação: \n"
                     "𝐶 = 𝑛! / (𝑝! ∗ (𝑛 − 𝑝)!) \n\n"
                     "3 - Sair do menu. \n\n"
                     "R: "))


def desenvolver_escolha():
    opcao = exibir_menu()
    if opcao == 1:
        n = int(input("Insira o primeiro número: "))
        p = int(input("Insira o primeiro número: "))
        calc_comb(n, p)
    else:
        n = int(input("Insira o primeiro número: "))
        p = int(input("Insira o primeiro número: "))
        calc_arranjo(n, p)


def calc_comb(x: int, y: int) -> int:
    return resultado == calc_fat(x) / calc_fat(x - y)


def calc_arranjo(x: int, y: int) -> int:
    return resultado == calc_fat(x) / calc_fat(y) * calc_fat(x - y)




# print(f"{nome}, o resultado do(a) {op_escolhida} dos números {n} e {p} será {resultado}")
