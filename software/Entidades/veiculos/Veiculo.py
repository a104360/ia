

class Veiculo:
    def __init__(self, name, capacidade, combustivel, time, tipo, id = -1):   
        self.id = id #id
        self.name = str(name) #nome do veiculo
        self.capacidade = capacidade #capacidade máxima de carga
        self.combustivel = combustivel #autonomia de combustivel
        self.time = time #tempos de viagem
        self.tipo = tipo #se e drone, helicóptero, barco, camiao, etc.

    def __str__(self):
        return "veiculo " + self.name

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
    def setCombustivel(self, combustivel):
        self.combustivel = combustivel

    def getCombustivel(self):
        return self.combustivel

    # Métodos para 'time'
    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    # Métodos para 'tipo'
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
