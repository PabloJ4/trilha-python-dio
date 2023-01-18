
consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (Residencia, Comercio ou Industria): ")
if tipo == "Residencia":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "Industria":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "Comercio":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Erro ! Tipo de instalação desonhecido!")
custo = consumo * preco
print(f"Valor a pagar: R$ {custo:10.2f}")