def calc_fat(x: int):
    if x == 1:
        return 1
    else:
        return x * calc_fat(x - 1)


def opcao() -> int:
    escolha = int(input("O que deseja calcular? "
                        "\n1 - Arranjos: "
                        "\n𝐴 = 𝑛! / (𝑛 − 𝑝)! \n"
                        "\n2 - Combinações: \n"
                        "𝐶 = 𝑛! / (𝑝! ∗ (𝑛 − 𝑝)!) "
                        "\n3 - Sair \n"
                        "R: "))

    return escolha


def desenv_op():
    if opcao() == 1:
        calc_comb()
    elif opcao() == 2:
        calc_arranjo()


def calc_comb() -> int:
    return calc_fat(n) / calc_fat(n - p)


def calc_arranjo() -> int:
    return calc_fat(n) / calc_fat(p) * calc_fat(n - p)


n = int(input("Insira o primeiro número: "))
p = int(input("Insira o primeiro número: "))

# print(f"{nome}, o resultado do(a) {op_escolhida} dos números {n} e {p} será {resultado}")
