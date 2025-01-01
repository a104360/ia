from . import Veiculo

class Carro(Veiculo.Veiculo):
    def __init__(self, name = "Road Man", id = -1, capacidade = 100, cargaAtual = 0, bens = {}, level = 150, limit = 300, combustivel = 8, tipo = "Barco"):
        super().__init__(name, id, capacidade, cargaAtual, bens, level, limit, combustivel, tipo)

    def __str__(self):
        return "\n(Carro)\n" + super().__str__()
    
    def getType(self):
        return "Carro"