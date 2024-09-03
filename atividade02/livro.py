class Livro:
    def __init__(self, ptitulo, pautor, ppaginas):
        self.titulo = ptitulo
        self.autor = pautor
        self.paginas = ppaginas
    def info(self):
        return f"O livro {self.titulo} do autor {self.autor} possui {self.paginas}"

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 323)
livro2 = Livro("A Culpa é das Estrelas", "John Green", 313)