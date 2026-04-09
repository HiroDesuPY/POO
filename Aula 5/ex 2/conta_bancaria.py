import random 

class Contabancaria:
    """Classe para representar uma conta bancária com operações de depósito, saque e verificação de saldo."""


    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"Conta: {self.id}\nTitular: {self.nome}\nSaldo: R${self.saldo:.2f}\nOla {self.nome}! Você deseja;\n1 - Depositar\n2 - Sacar\n3 - Verificar Saldo\n4 - Sair"
    
    
    def escolha(self):
        while True:
            try:
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    valor = float(input("Digite o valor a ser depositado: "))
                    self.saldo += valor
                    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
                    continue
                elif opcao == 2:
                    valor = float(input("Digite o valor a ser sacado: "))
                    if valor > self.saldo:
                        print("Saldo insuficiente para saque.")
                        continue
                    else:
                        self.saldo -= valor
                        print(f"Saque de R${valor:.2f} realizado com sucesso!")
                        continue
                elif opcao == 3:
                    print(f"Saldo atual: R${self.saldo:.2f}",)
                    continue
                elif opcao == 4:
                    print(f"Obrigado por usar nossos serviços, {self.nome}! Até a próxima.")
                    break
                else:
                    raise ValueError("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
                
            except ValueError as e:
                print(e)
                continue 

    


# random.seed(42) 
conta = Contabancaria(id = random.randint(100, 999), nome= random.choice(["João", "Maria", "Carlos"]), saldo= random.uniform(1000, 9999))
print (conta)
conta.escolha()
print(conta.__doc__)

