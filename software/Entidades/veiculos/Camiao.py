import Veiculo

class Camiao(Veiculo.Veiculo):
    def __init__(self,capacidade = 110,combustivel = 50,name = "Road Runner",id = -1):
        super().__init__(name,capacidade,id,combustivel)

    def __str__(self):
        return "\n(Camiao)\n" + super().__str__()
    
    def getType(self):
        return "Camiao"