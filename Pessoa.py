#Crie uma clase "pessoa" que tenha atributos como nome, idade, endereço. Adicione métods ]á classe para
#definir e obter esses atributos. Crie várias instancias da classe e imprima os valores de cada instancia.
class Pessoa:
    def __init__(self,nome:str, idade:int,endereco:str):
        self.nome =nome
        self.idade =idade
        self.endereco =endereco
    
    def definir_nome(self, novo_nome):
        self.nome =novo_nome

    def obter_nome(self):
        return self.nome

    def definir_idade(self, nova_idade):
        self.idade = nova_idade

      
    def definir_endereco(self, novo_enderco:str):
        self._endereco = novo_enderco


    def obter_enderco(self):
        return self.endereco
