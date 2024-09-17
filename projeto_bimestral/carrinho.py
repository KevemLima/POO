from item import Item

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def mostrar_carrinho(self):
        if not self.itens:
            return "Seu carrinho está vazio."
        resultado = "\n".join(str(item) for item in self.itens)
        total = self.calcular_total()
        return f"{resultado}\nTotal: R${total:.2f}"

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def finalizar_pedido(self):
        if not self.itens:
            return "Seu carrinho está vazio. Não há o que finalizar."
        resultado = "\n".join(str(item) for item in self.itens)
        total = self.calcular_total()
        return f"Itens comprados:\n{resultado}\nTotal: R${total:.2f}\n\n1. Confirmar pedido\n2. Voltar"