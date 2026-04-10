class Pessoa:
    def __init__ (self, nome, idade, data_aniversario):
        self.nome = nome
        self.idade = idade
        self.data_aniversario = data_aniversario

    def aniversario (self):
        self.idade += 1
