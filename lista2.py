#Faça um programa que leia uma lista de 5 núemros inteiros e mostre-os
listaNumeros =[]
print("Informe os 5 numeros")
for i in range (5):
    listaNumeros.append(input("Numeros"+str(i+1)+":\n"))

print(listaNumeros)