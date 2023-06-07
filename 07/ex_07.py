def soma(x: int, y: int, z: int):
    return x + y + z


def escolha_sabor():
    sabor = int(input("Defina o tipo do sabor da pizza: \n1 - Normal - 15 "
                      "reais \n2 - Gourmet - 20 reais \n3 - Premium - 30 reais \nR: "))
    if sabor == 1:
        return 15
    elif sabor == 2:
        return 20
    else:
        return 30


valor = soma(escolha_sabor(), escolha_sabor(), escolha_sabor())

print(f"{valor}")