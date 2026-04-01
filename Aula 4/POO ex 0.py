class Primeira_Classe:
    def __init__(self):
       self.nome = ""
       self.idade = 0
       self.cidade = ""
       self.aniver = ""

    def aniversario (self):
        self.idade += 1

    def conclusao (self):
        print (f'{self.nome} de cidade {self.cidade} tem {self.idade} anos de idade')



data = "06/12"
p1 = Primeira_Classe()
p1.nome = input("Digite o nome: ")
p1.cidade = input("Digite a cidade: ")
p1.idade = int(input("Digite a idade: "))
p1.aniver = input("Digite a data de aniversário: ")

if p1.aniver == data:
    p1.aniversario()

p1.conclusao()