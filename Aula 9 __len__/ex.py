class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    # Implementando o Dunder Method __len__
    def __len__(self):
        return len(self.produtos)

# --- Uso ---
meu_carrinho = CarrinhoDeCompras()
meu_carrinho.adicionar("Notebook")
meu_carrinho.adicionar("Mouse")

# Sem o __len__, você teria que acessar o atributo: print(len(meu_carrinho.produtos))
# Com o __len__ definido, você usa a função len() diretamente no objeto:
print(f"Itens no carrinho: {len(meu_carrinho)}") 