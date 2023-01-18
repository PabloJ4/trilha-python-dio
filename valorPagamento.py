def valorPagamento(valor, dias):
    juros_atraso=0
    if dias == 0:
        return valor
    else:
        juros_atraso =0.1*dias
        return valor+((3*valor)/100)+juros_atraso
valor_total=0
contador=0

while True:
    valor=float(input("Informe o valor da prestação:"))
    if valor==0:
        break
    dias=int(input("informe a quantidade de dias em atraso:"))
    valor_total+=valorPagamento(valor,dias)
    contador=contador+1

print('Quantidade total: %d' % contador)
print('Valor total das prestações: %.2f' % valor_total)




