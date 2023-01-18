#Escreva um programa que pergunta a velocidade de um carro. Caso
# ultrapsse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$5 por cada km acima
# da velocidade permitida.

velocidade=float(input("Informe a velocidade do veiculo em KM: "))

multa=(velocidade-80)*5

if (velocidade>80):
    print("VOCÊ FOI MULTADO")
    print(f'O usuário foi multado em {multa:7.5}')
elif (velocidade<80):
    print("Você está andando na velocidade permitida")
#else:
   # print("Continue Dirigindo")


