while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        fator1 = int(input("Tabuada de:"))
        fator2 = 1
        while fator2 <= 10:
            if opção == 1:
                print(f"{fator1} + {fator2} = {fator1 + fator2}")
            elif opção == 2:
                print(f"{fator1} - {fator2} = {fator1 - fator2}")
            elif opção == 3:
                print(f"{fator1} / {fator2} = {fator1 / fator2:5.4f}")
            elif opção == 4:
                print(f"{fator1} x {fator2} = {fator1 * fator2}")
            fator2 = fator2 + 1
    else:
        print("Opção inválida!")