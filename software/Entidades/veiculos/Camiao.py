from . import Veiculo


class Camiao(Veiculo.Veiculo):
    def __init__(self, name = "Camiao", id = -1, capacidade = 300, cargaAtual = 0, bens = {}, level = 400, limit = 800, combustivel = 18, tipo = "terra"):
        super().__init__(name, id, capacidade, cargaAtual, bens, level, limit, combustivel, tipo)

    def __str__(self):
        return "\n(Camiao)\n" + super().__str__()
    
    #def getType(self):
    #    return "terra"