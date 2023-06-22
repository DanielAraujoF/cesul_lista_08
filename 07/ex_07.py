def soma(x: int, y: int, z: int):
    return x + y + z


def escolha_sabor():
    sabor = int(input("Defina o tipo do sabor da pizza: \n"
                      "1 - Normal - 15 reais \n"
                      "2 - Gourmet - 20 reais \n"
                      "3 - Premium - 30 reais \n"
                      "R: "))
    if sabor == 1:
        return 15
    elif sabor == 2:
        return 20
    elif sabor == 3:
        return 30
    else:
        while sabor != 1 or sabor != 2 or sabor != 3:
            print("Nenhum sabor corresponde ao inserido. Tente novamente:")
            escolha_sabor()
            if sabor != 1 or sabor != 2 or sabor != 3:
                break


valor = soma(escolha_sabor(), escolha_sabor(), escolha_sabor())

print(f"{valor}")