mercadoria =float(input("Informe o valor da mercadoria\n:"))
p_desconto =float(input("Informe a porcentagem de desconto:\n"))

novo_preco=mercadoria-(mercadoria*p_desconto)
desconto=mercadoria*p_desconto

print(f'O desconto foi de {desconto}R$.')
print(f'A.pós desconto o preço foi ajustado para {novo_preco}R$')