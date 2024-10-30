class Moto:
    def __init__(self, pmarca, pmodelo, pcilindradas):
        self.marca = pmarca
        self.modelo = pmodelo
        self.cilindradas = pcilindradas
    def dados(self):
        return f"A moto {self.modelo} possui {self.cilindradas} cilindradas"

moto1 = Moto("Honda", "Honda CB 500F", 500)
moto2 = Moto("Yamaha", "Yamaha YZF-R6", 600)