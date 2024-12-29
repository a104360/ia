import Combustivel

class Veiculo:
    def __init__(self, name, capacidade, id = -1,combustivel = 150, tipo = None):   
        self.id = id #id
        self.name = str(name) #nome do veiculo
        self.capacidade = capacidade #capacidade máxima de carga
        self.combustivel = Combustivel.Combustivel(combustivel,75,9) #autonomia de combustivel
        self.tipo = tipo #se e drone, helicóptero, barco, camiao, etc.

    def __str__(self):
        return f"ID : {self.id}\nNome : {self.name}\nCarga maxima : {self.capacidade}\n" + self.combustivel.__str__()

    def __repr__(self):
        return "veiculo " + self.name

    # Métodos para 'id'
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    # Métodos para 'name'
    def setName(self, name):
        self.name = str(name)

    def getName(self):
        return self.name

    # Métodos para 'capacidade'
    def setCapacidade(self, capacidade):
        self.capacidade = capacidade

    def getCapacidade(self):
        return self.capacidade

    # Métodos para 'combustivel'
    def walkedKm(self,km:int):
        """Removes the liters equivalent to the amount of miles travelled"""
        self.combustivel.spend(km)

    def refuel(self,liters : int):
        """Fills the fuel tank with the indicated liters"""
        self.combustivel.fill(liters)

    def getAutonomy(self):
        """Returns how many Km the vehicle can drive"""
        return self.combustivel.getAutonomy()

    # Métodos para 'tipo'
    def setTipo(self, tipo):
        self.tipo = tipo

    def getType(self):
        return None
         
