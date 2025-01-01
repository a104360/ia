from . import Combustivel
from .Carga import Carga
from . import Bem

class Veiculo:
    def __init__(self, name, id = -1, capacidade = 100, cargaAtual = 0, bens = {}, level = 150, limit = 300, consumption = 10, tipo = None):   
        """
            id - valor único de cada veiculo

            name - nome do veiculo

            capacidade - carga do veiculo

            combustivel - autonomia de combustivel

            tipo - se e drone, helicóptero, barco, camiao, etc.
        """
        self.id = id
        self.name = str(name)
        self.capacidade = Carga(capacidade, cargaAtual, bens)
        self.combustivel = Combustivel.Combustivel(level, limit, consumption)
        self.tipo = tipo

    def __str__(self):
        return f"ID : {self.id}\nNome : {self.name}\nCarga maxima : {self.capacidade}\n" + self.combustivel.__str__()

    def __repr__(self):
        return self.__str__()#"veiculo " + self.name

    # Métodos para 'id'
    def setId(self, id : int):
        self.id = id

    def getId(self):
        return self.id

    # Métodos para 'name'
    def setName(self, name : str):
        self.name = name

    def getName(self):
        return self.name

    # Métodos para 'capacidade'
    def loadCarga(self, bens: list[Bem.Bem]):
        """Adiciona bens ao veiculo"""
        self.capacidade.restock(bens)

    def takeCarga(self, bens: list[Bem.Bem]):
        """Retira bens ao veiculo"""
        return self.capacidade.distribute(bens)
    
    def getCargaAvailable(self):
        """Returns a carga disponivel do veiculo"""
        return self.capacidade.getCargaDisponivel()
    
    def getBensAvailable(self):
        """Returns os bens do veiculo"""
        return self.capacidade.getBens()

    # Métodos para 'combustivel'
    def walkedKm(self, km : int):
        """Removes the liters equivalent to the amount of miles travelled"""
        self.combustivel.spend(km)

    def refuel(self, liters : int):
        """Fills the fuel tank with the indicated liters"""
        self.combustivel.fill(liters)

    def getAutonomy(self):
        """Returns how many Km the vehicle can drive"""
        return self.combustivel.getAutonomy()

    # Métodos para 'tipo'
    def setTipo(self, tipo : str):
        self.tipo = tipo

    def getType(self):
        return None
        
