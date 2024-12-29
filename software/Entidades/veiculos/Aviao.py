import Veiculo

class Aviao(Veiculo.Veiculo):
    def __init__(self,capacidade = 200,combustivel = 50,name = "Falcon",id = -1,time = 10):
        super().__init__(name,capacidade,id,combustivel)
    
    def __str__(self):
        return "\n(Aviao)\n" + super().__str__()
    
    def getType(self):
        return "Aviao"