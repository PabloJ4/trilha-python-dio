#Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. 
#Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
#Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
x = 1
r = 0
while x <= n2:
    r = r + n1
    x = x + 1
print(f"{n1} x {n2} = {r}")