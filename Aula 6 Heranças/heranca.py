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


a1 = Aluno(nome="João", idade=20, data_aniversario="01/01/2003", curso= "Engenharia", matricula="12345")
a1.aniversario()
a1.matricular()
print (a1.__dict__)

p1 = Professor(nome="Maria", idade=40, data_aniversario="15/05/1983", especialidade="Matemática", nivel="Doutorado")
p1.dando_aula()

f1 = Funcionario(nome="Carlos", idade=30, data_aniversario="10/10/1993", cargo="Analista", setor="TI")
f1.bater_ponto()