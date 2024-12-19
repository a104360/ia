import Veiculo

class Barco(Veiculo.Veiculo):
    def __init__(self,capacidade = 110,combustivel = 50,name = "Trailblazer",id = -1,time = 10):
        super().__init__(name,capacidade,id,combustivel)