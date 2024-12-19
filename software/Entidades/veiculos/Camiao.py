import Veiculo

class Camiao(Veiculo.Veiculo):
    def __init__(self,name = "Road Runner",capacidade = 110,combustivel = 50,time = 10):
        super().__init__(name,capacidade,combustivel,time,"Camiao")