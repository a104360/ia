import Veiculo

class Barco(Veiculo.Veiculo):
    def __init__(self, name = "Trailblazer", id = -1, capacidade = 150, cargaAtual = 0, bens = {}, level = 200, limit = 400, combustivel = 12, tipo = "Barco"):
        super().__init__(name, id, capacidade, cargaAtual, bens, level, limit, combustivel, tipo)

    def __str__(self):
        return "\n(Barco)\n" + super().__str__()
    
    def getType(self):
        return "Barco"