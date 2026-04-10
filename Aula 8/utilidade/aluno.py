from utilidade.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome, idade, data_aniversario, curso, matricula):
        super().__init__(nome, idade, data_aniversario)
        self.curso = curso
        self.matricula = matricula

    def matricular (self):
        print (f'{self.nome} matriculado no curso de {self.curso} com matrícula {self.matricula}')
