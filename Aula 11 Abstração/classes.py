from abc import ABC, abstractclassmethod #abstract base class

class Pessoa(ABC):
    def __init__ (self, nome, idade, data_aniversario):
        self.nome = nome
        self.idade = idade
        self.data_aniversario = data_aniversario

    def aniversario (self):
        self.idade += 1

    @abstractclassmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self,nome, idade, data_aniversario, curso, matricula):
        super().__init__(nome, idade, data_aniversario)
        self.curso = curso
        self.matricula = matricula

    def matricular (self):
        print (f'{self.nome} matriculado no curso de {self.curso} com matrícula {self.matricula}')
    
    def estudar(self):
        print (f"{self.nome} está estudando no curso de {self.curso}")


class Professor(Pessoa):
    def __init__(self, nome, idade, data_aniversario, especialidade, nivel):
        super().__init__(nome, idade, data_aniversario)
        self.especialidade = especialidade
        self.nivel = nivel

    def dando_aula (self):
        print (f'{self.nome} está dando aula de {self.especialidade} com nível {self.nivel}')

    def estudar(self):
        print (f"{self.nome} é especializado no {self.especialidade}")



class Funcionario(Pessoa):
    def __init__(self, nome, idade, data_aniversario, cargo, setor):
        super().__init__(nome, idade, data_aniversario)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto (self):
        print (f'{self.nome} bateu ponto como {self.cargo} no setor {self.setor}')

    def estudar(self):
        print (f"{self.nome} é especializado no {self.setor}")