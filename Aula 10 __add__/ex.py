class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    # Dunder method para definir a representação em string
    def __str__(self):
        return f"'{self.titulo}' tem {self.paginas} páginas."

    # Dunder method para permitir somar as páginas de dois livros
    def __add__(self, outro_livro):
        return self.paginas + outro_livro.paginas

# Uso
livro1 = Livro("Python Fluente", 500)
livro2 = Livro("Clean Code", 400)

print(livro1)  # Chama o __str__
print(livro1 + livro2)  # Chama o __add__ (resulta em 900)