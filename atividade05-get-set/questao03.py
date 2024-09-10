class Funcionario:
  def __init__(self, nome, cargo, salario):
    self.__nome = nome
    self.__cargo = cargo
    self.__salario = salario

  def get_nome(self):
    return self.__nome

  def set_nome(self, nome):
    self.__nome = nome

  def get_cargo(self):
    return self.__cargo

  def set_cargo(self, cargo):
    self.__cargo = cargo

  def get_salario(self):
    return self.__salario

  def set_salario(self, salario):
    self.__salario = salario

nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario = input("Digite o salário do funcionário: ")

funcionario1 = Funcionario(nome, cargo, salario)

print(f"O nome do funcionário é: {funcionario1.get_nome()}")
print(f"O cargo do funcionário é: {funcionario1.get_cargo()}")

novocargo = input("Digite um novo cargo para o funcionário: ")
funcionario1.set_cargo(novocargo)

print("O novo cargo do funcionário é: ", funcionario1.get_cargo())