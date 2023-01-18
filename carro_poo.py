#Crie uma classe "Carro" com atributos como marca, modelo e ano. Adicione um método "andar" à  classe.
#que imprima uma mensagem dizendo que o carro esta andando.
#Crie uma classe "concessionaria" que tem varias instancias da classe "Carro" com atributos.
#Adicione um metodo à classe concessionaria que liste todos os carros que ela possui.

class Carro:
  def __init__(self,marca:str, modelo:str, ano: int):
    self.marca = marca  
    self.modelo = modelo
    self.ano = ano

  def Andar(self, ligado: str):
    print(f'Meu carro da marca {self.marca} é um modelo da {self.modelo} do ano de {self.ano}')
    print("verificar se o carro está ligado")
    print(f'O carro esta ligado: {ligado}')
    print("Sai de primeira e está andando")

class Concessionaria:
    def __init__(self):
        self.carros=[]

    def adicionar_carros():
    

    def listar_carros(self):
        for carro in self.carros:
            print("Marca:", carro.marca)
            print("Modelo:", carro.modelo)
            print("Ano:", carro.ano)

carro1 =Carro("Ford", "Fiesta", 2020)


concessionaria = Concessionaria()
concessionaria.adicionar_carro(carro1)