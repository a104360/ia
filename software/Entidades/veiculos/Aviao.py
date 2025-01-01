from . import Veiculo

class Aviao(Veiculo.Veiculo):
    def __init__(self, name = "Falcon", id = -1, capacidade = 300, cargaAtual = 0, bens = {}, level = 300, limit = 450, combustivel = 15, tipo = "Aviao"):
        super().__init__(name, id, capacidade, cargaAtual, bens, level, limit, combustivel, tipo)
    
    def __str__(self):
        return "\n(Aviao)\n" + super().__str__()
    
    def getType(self):
        return "Aviao"