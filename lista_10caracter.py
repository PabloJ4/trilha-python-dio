#Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.

listaChar = []
consoantes = 0
print ('Informe os caracters')
for i in range(10):
 	listaChar.append((input('Caracter  '+ str(i+1) + ':\n')))
char = listaChar[i]
if(char not in ('a','e','i','o','u')):
 		consoantes += 1
print(consoantes)
   
