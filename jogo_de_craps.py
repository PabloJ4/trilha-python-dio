import random
# Jogo de Craps. Faca um programa de implemente um jogo de Craps. O jogador
# lanca um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada,
# voce tirar 7 ou 11, voce tirou um "natural" e ganhou. Se voce tirar 2, 3 ou
# 12 na primeira jogada, isto e chamado de "craps" e voce perdeu. Se, na
# primeira jogada, voce fez um 4, 5, 6, 8, 9 ou 10,este e seu "Ponto". Seu
# objetivo agora e continuar jogando os dados ate tirar este numero novamente.
# Voce perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
# Dica: para simular o lancamento do dado, utilize o metodos Random do Python.!

a="Você ganhou, parabéns\n"
b="\n\n\t***** Craps! *****\n\nVocê perdeu!!!\tTente de novo\n"
c="Ponto\n"
def craps():
 dado1=random.randrange(1,7)
 dado2=random.randrange(1,7)
 soma=dado1+dado2
 print("Dado 1: ",dado1)
 print("Dado 2: ",dado2)
 print("A soma dos dados é: ",soma,"\n")
 return soma
print("*****GAME - CRAPS*****")
while True:
 jogar=input("Rolar dados (s ou n)? ")
 if jogar=='n' or jogar=='N':
     break
 else:
  result=craps()
  if result==7 or result==11:
    print(a)
  elif result==2 or result==3 or result==12:
    print(b)
  else:
   print(c)
 while True:
  result2=craps()
  if result==result2:
    print(a)
    break
  elif result2==7:
    print(b)
    break
  else:
   print("Ainda não foi dessa vez!\nSEGUE O JOGO!!!!\n")