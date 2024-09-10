class Retangulo:
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    def get_largura(self):
        return self.__largura

    def set_largura(self, largura):
        self.__largura = largura

    def get_altura(self):
        return self.__altura

    def set_largura(self, altura):
        self.__altura = altura

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = largura*altura

retangulo = Retangulo(largura, altura)

print(f"A largura do seu retângulo é {retangulo.get_largura()} m")
print(f"A altura do seu retângulo é {retangulo.get_altura()} m")
print(f"A área do seu retângulo é {area} m²")