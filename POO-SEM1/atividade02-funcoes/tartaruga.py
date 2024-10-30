class Tartaruga:
    def __init__(self, nome, posicao_x, posicao_y):
        self.nome = nome
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    def andar_para_frente(self, passos):
        self.posicao_x = self.posicao_x + passos

    def andar_para_tras(self, passos):
        self.posicao_x = self.posicao_x - passos

    def andar_para_cima(self, passos):
        self.posicao_y = self.posicao_y + passos

    def andar_para_baixo(self, passos):
        self.posicao_y = self.posicao_y - passos

    def onde_estou(self):
        return f"Eu sou a tartaruga {self.nome} e estou na posição x: {self.posicao_x}. E estou na posição y: {self.posicao_y}"

tartaruga = Tartaruga("Mano Brown", 0, 0)

tartaruga.andar_para_frente(10)
tartaruga.andar_para_tras(20)
tartaruga.andar_para_cima(30)
tartaruga.andar_para_baixo(40)