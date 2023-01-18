class Pessoa:
    def __init__(self,nome:str, idade:int,altura:float):
        self.nome =nome
        self.idade =idade
        self.altura =altura
    def dizer_ola(self):
        print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} anos e minha altura é {self.altura}')
    
    def Cozinhar(self, receita:str):
        print(f"Estou cozinhando um(a): {receita}")

    def andar(self, distancia: float):
        print(f"Sai para andar. Volto quando completar {distancia} metros")

# Instancia um objeto da Classe "Pessoa"
pessoa=Pessoa(nome="João", idade=25, altura=1.88)

#Chamamos os metodos de "Pessoa"
pessoa.dizer_ola()
pessoa.Cozinhar('spaghetti')
pessoa.andar(750.5)
