class Produto:
  def __init__(self, nome, preco, quantidade):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

  def get_nome(self):
    return self.nome

  def set_nome(self):
    self.nome = nome

  def get_preco(self):
    return self.preco

  def set_preco(self):
    self.preco = preco

  def get_quantidade(self):
    return self.quantidade

  def set_quantidade(self):
    self.quantidade = quantidade

nome = input("Digite o nome do produto: ")
preco = input("Digite o preço do produto: ")
quantidade = input("Digite a quantidade do produto: ")
produto1 = Produto(nome, preco, quantidade)
print(produto1.get_nome())