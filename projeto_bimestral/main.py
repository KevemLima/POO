from carrinho import Carrinho
from item import Item

class Lanchonete:
    def __init__(self):
        self.carrinho = Carrinho()
        self.menu = [
            Item("Hambúrguer", 12.00),
            Item("Batata Frita", 8.00),
            Item("Refrigerante", 5.00),
            Item("Pizza", 20.00)
        ]

    def mostrar_menu(self):
        return "\n".join(f"{i+1}. {item}" for i, item in enumerate(self.menu))

    def executar(self):
        while True:
            print("\nBem-vindo à Lanchonete!")
            print("1. Ver carrinho")
            print("2. Adicionar ao carrinho")
            print("3. Finalizar pedido")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                print(self.carrinho.mostrar_carrinho())
            elif escolha == '2':
                print("Escolha um item para adicionar ao carrinho:")
                print(self.mostrar_menu())
                escolha_item = int(input("Digite o número do item: ")) - 1
                if 0 <= escolha_item < len(self.menu):
                    item = self.menu[escolha_item]
                    self.carrinho.adicionar_item(item)
                    print(f"{item.nome} adicionado ao carrinho.")
                else:
                    print("Escolha inválida.")
            elif escolha == '3':
                resultado = self.carrinho.finalizar_pedido()
                print(resultado)
                if "Confirmar pedido" in resultado:
                    confirmacao = input("Escolha uma opção: ")
                    if confirmacao == '1':
                        print("Pedido confirmado! Bom apetite!")
                        break
                    elif confirmacao == '2':
                        continue
                    else:
                        print("Opção inválida.")
                else:
                    print("Não há itens para finalizar.")
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    lanchonete = Lanchonete()
    lanchonete.executar()
