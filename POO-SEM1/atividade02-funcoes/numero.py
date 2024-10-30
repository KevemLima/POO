class Numero:
    def __init__(self, num):
        self.num = num

    def sucessor(self):
        valor = self.num + 1
        return f"O sucessor de {self.num} é {valor}"

    def antecessor(self):
        valor = self.num - 1
        return f"O antecessor de {self.num} é {valor}"

    def dobro(self):
        valor = self.num * 2
        return f"O dobro de {self.num} é {valor}"

    def triplo(self):
        valor = self.num * 3
        return f"O triplo de {self.num} é {valor}"

    def metade(self):
        valor = int(self.num / 2)
        return f"A metade de {self.num} é {valor}"

numero1 = Numero(2)
numero2 = Numero(8)