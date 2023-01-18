#Escreva um programa que leia tres numeros e que imprima o maior e menor
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))

maior = n1
menor = n1

if maior < n2:
	maior = n2

if maior < n3: 
	maior = n3

if menor > n2:
	menor = n2

if menor > n3:
	menor = n3

print ('Maior:  %d ' %maior)
print ('Menor:  %d ' %menor)
