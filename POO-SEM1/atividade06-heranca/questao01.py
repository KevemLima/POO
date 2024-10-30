class Pessoa:
    nome = None

    def __init__(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    cargo = None

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo


funcionario1 = Funcionario("Kevem")

funcionario1.set_cargo("Info")

print(funcionario1.nome, funcionario1.cargo)