import aluno
import veiculo
import produto
import animal

##objetos alunos
a1 = aluno.Aluno("Kevem","Infoweb", "2°Ano")
a2 = aluno.Aluno("Douglas","Comercio", "1°Ano")
a3 = aluno.Aluno("Vinicius","Eletro", "3°Ano")

a1.serie = "3°Ano"
a2.serie = "4°Ano"

#print(a1.serie, a2.serie)

##objetos veiculos
v1 = veiculo.Veiculo("Ford","Mustang GT500", 1967)
v2 = veiculo.Veiculo("Volkswagen","Gol", 2015)

v1.fabricante = "Voyage"

#print(v1.fabricante)

##objetos produtos
p1 = produto.Produto("Notebook", "3500,00", 10)
p2 = produto.Produto("Mouse", "50,00", 100)

p1.preco = "3800,00"

#print(p1.preco)

##objetos animais
an1 = animal.Animal("Rex","Cachorro", 3)
an2 = animal.Animal("Mimosa","Gato", 5)

an1.idade = 10

print(an1.idade)