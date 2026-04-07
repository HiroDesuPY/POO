class Primeira_Classe:
    """
    Essa classe identifica uma pessoa, com nome, idade, cidade e data de aniversário. Ela tem um método para fazer aniversário, aumentando a idade em 1, e um método para mostrar as informações da pessoa.
    """
    def __init__(self, n, i, c, a): #dunder instanciation method
       self.nome = n
       self.idade = i
       self.cidade = c
       self.aniver = a

    def aniversario (self):
        self.idade += 1

    def __str__(self): #dunder method
        return f'{self.nome} de cidade {self.cidade} tem {self.idade} anos de idade'



data = "06/12"
p1 = Primeira_Classe(n=input("Digite o nome: "), i=int(input("Digite a idade: ")), c=input("Digite a cidade: "), a =input("Digite a data de aniversário: "))
# p1.nome = input("Digite o nome: ")
# p1.cidade = input("Digite a cidade: ")
# p1.idade = int(input("Digite a idade: "))
# p1.aniver = input("Digite a data de aniversário: ")

if p1.aniver == data:
    p1.aniversario()

print(p1)
print (p1.__doc__)
print (p1.__dict__) #dicionario de atributos e métodos da classe
# print (Primeira_Classe.__getstate__()) #personalizável