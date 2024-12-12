

class Recurso:
    def __init__(self, name, tipo, validade, id = -1):     #  construtor do nodo....."
        self.id = id #id
        self.name = str(name) #nome do recurso
        self.tipo = tipo #se e comida, medicamento etc
        self.validade = validade #tempo de validade

    def __str__(self):
        return "recurso " + self.name

    def __repr__(self):
        return "recurso " + self.name

    # Métodos para 'id'
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    # Métodos para 'name'
    def getName(self):
        return self.name

    # Métodos para 'tipo'
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    # Métodos para 'validade'
    def setValidade(self, validade):
        self.validade = validade

    def getValidade(self):
        return self.validade

