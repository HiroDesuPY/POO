from utilidade.pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, data_aniversario, especialidade, nivel):
        super().__init__(nome, idade, data_aniversario)
        self.especialidade = especialidade
        self.nivel = nivel

    def dando_aula (self):
        print (f'{self.nome} está dando aula de {self.especialidade} com nível {self.nivel}')
