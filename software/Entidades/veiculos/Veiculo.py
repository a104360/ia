from . import Combustivel
from .Carga import Carga
from . import Bem

class Veiculo:
    def __init__(self, name, id, capacidade = 100, cargaAtual = 0, bens = {}, level = 150, limit = 300, consumption = 10, tipo = None):   
        """
            id - valor único de cada veiculo

            name - Helicoptero, Barco, Carro, Camiao, Aviao

            capacidade - carga do veiculo

            combustivel - autonomia de combustivel

            tipo - Terra | Mar | Ar
        """
        self.id = id
        self.name = str(name)
        self.carga = Carga(capacidade, cargaAtual, bens)
        self.combustivel = Combustivel.Combustivel(level, limit, consumption)
        self.tipo = tipo

    def to_dict(self):
        return {
            "id":self.id,
            "name" : self.name,
            "carga": self.carga.__dict__,
            "combustivel" : self.combustivel.__dict__,
            "tipo" : self.tipo
        }
    
    def from_dict(self,dict):
        #tipo = dict["name"]
        #if tipo == "Helicoptero":
        return Veiculo(
            dict["name"],
            dict["id"],
            dict["carga"]["maxCarga"],
            dict["carga"]["cargaAtual"],
            dict["carga"]["bens"],
            dict["combustivel"]["level"],
            dict["combustivel"]["limit"],
            dict["combustivel"]["consumption"],
            #Carga(1).from_dict(dict["carga"]),
            #Combustivel.Combustivel(1,2).from_dict(dict["combustivel"]),
            dict["tipo"]
        )
            


    def __str__(self):
        return f"ID : {self.id}\nNome : {self.name}\nCarga maxima : {self.carga}\n" + self.combustivel.__str__()

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
        self.carga.restock(bens)

    def takeCarga(self, bens: list[Bem.Bem]):
        """Retira bens ao veiculo"""
        return self.carga.distribute(bens)
    
    def getCargaAvailable(self):
        """Returns a carga disponivel do veiculo"""
        return self.carga.getCargaDisponivel()
    
    def getBensAvailable(self):
        """Returns os bens do veiculo"""
        return self.carga.getBens()

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
        return self.tipo