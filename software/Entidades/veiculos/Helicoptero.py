from . import Veiculo

class Helicoptero(Veiculo.Veiculo):
    def __init__(self, name = "Air Runner", id = -1, capacidade = 200, cargaAtual = 0, bens = {}, level = 150, limit = 300, combustivel = 10, tipo = "Helicoptero",velocidade = 150):
        super().__init__(name, id, capacidade, cargaAtual, bens, level, limit, combustivel, tipo, velocidade)

    def __str__(self):
        return "\n(Helicoptero)\n" + super().__str__()
    
    def getType(self):
        return "Helicoptero"