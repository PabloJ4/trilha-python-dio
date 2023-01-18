
hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))

def converter_hora(hora):
    return (hora -12)

def imprime_hora(hora,minuto):
    if(hora <= 12):
        print(hora,minuto)
    else:
        print(converter_hora(hora), minuto)

#imprime_hora(hora, minuto)
controle = 1
while controle != 0:
    print(imprime_hora(hora, minuto))
    controle = int(input("Continuar? 1(sim)/0(nao): "))








