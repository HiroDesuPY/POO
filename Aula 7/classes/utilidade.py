
class Pessoa:
    def __init__ (self, nome, idade, data_aniversario):
        self.nome = nome
        self.idade = idade
        self.data_aniversario = data_aniversario

    def aniversario (self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self,nome, idade, data_aniversario, curso, matricula):
        super().__init__(nome, idade, data_aniversario)
        self.curso = curso
        self.matricula = matricula

    def matricular (self):
        print (f'{self.nome} matriculado no curso de {self.curso} com matrícula {self.matricula}')
    

class Professor(Pessoa):
    def __init__(self, nome, idade, data_aniversario, especialidade, nivel):
        super().__init__(nome, idade, data_aniversario)
        self.especialidade = especialidade
        self.nivel = nivel

    def dando_aula (self):
        print (f'{self.nome} está dando aula de {self.especialidade} com nível {self.nivel}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, data_aniversario, cargo, setor):
        super().__init__(nome, idade, data_aniversario)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto (self):
        print (f'{self.nome} bateu ponto como {self.cargo} no setor {self.setor}')