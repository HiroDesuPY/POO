from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def main():
    a1 = Aluno(nome="João", idade=20, data_aniversario="01/01/2003", curso= "Engenharia", matricula="12345")
    a1.aniversario()
    a1.matricular()
    print (a1.__dict__)

    p1 = Professor(nome="Maria", idade=40, data_aniversario="15/05/1983", especialidade="Matemática", nivel="Doutorado")
    p1.dando_aula()

    f1 = Funcionario(nome="Carlos", idade=30, data_aniversario="10/10/1993", cargo="Analista", setor="TI")
    f1.bater_ponto()


if __name__ == "__main__":
    main()