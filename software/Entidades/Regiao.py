# Classe nodo para definiçao dos nodos

class Regiao:
    def __init__(self, name,gravidade, x, y, z, densidade, acesso, ambiente, id = -1):     #  construtor do nodo....."
        self.id = id #id
        self.name = str(name) #nome da regiao
        self.gravidade = gravidade #o quao prioritaria esta regiao é sendo 1 o que maior gravidade tem (depois pode ser mudado)
        self.x = x #coordenadas x
        self.y = y #coordenadas y
        self.z = z #coordenadas z
        self.densidade = densidade #densidade populacional
        self.acesso = acesso #acesso fasil ou dificil
        self.ambiente = ambiente #meio ambiente(chuva, sol, etc)
        self.necessidades = [] #recursos que a regiao necessita (pode ser uma lista com o recurso juntamente com o tempo max a que ele pode chegar ou separar em 2 listas)

    def __str__(self):
        return "regiao " + self.m_name

    def __repr__(self):
        return "regiao " + self.m_name

     # Métodos para 'id'
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    # Métodos para 'name'
    def getName(self):
        return self.name

    # Métodos para 'x'
    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    # Métodos para 'y'
    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    # Métodos para 'z'
    def setZ(self, z):
        self.z = z

    def getZ(self):
        return self.z

    # Métodos para 'densidade'
    def setDensidade(self, densidade):
        self.densidade = densidade

    def getDensidade(self):
        return self.densidade

    # Métodos para 'acesso'
    def setAcesso(self, acesso):
        self.acesso = acesso

    def getAcesso(self):
        return self.acesso

    # Métodos para 'ambiente'
    def setAmbiente(self, ambiente):
        self.ambiente = ambiente

    def getAmbiente(self):
        return self.ambiente

    # Métodos para 'necessidades'
    def setNecessidades(self, necessidades):
        """
        Define as necessidades da região. Aceita uma lista de objetos do tipo Recurso.
        """
        self.necessidades = necessidades

    def getNecessidades(self):
        """
        Retorna a lista de necessidades da região.
        """
        return self.necessidades

    def addNecessidade(self, recurso):
        """
        Adiciona um recurso à lista de necessidades da região.
        """
        self.necessidades.append(recurso)

    def removeNecessidade(self, recurso):
        """
        Remove um recurso da lista de necessidades da região, se existir.
        """
        if recurso in self.necessidades:
            self.necessidades.remove(recurso)