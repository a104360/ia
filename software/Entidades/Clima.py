class Clima:
    def __init__(self, tipo, id = -1, bloqueante = False, probabilidade = 0):
        """
        Classe base para representar diferentes tipos de clima.
        
        id - valor único de cada clima

        tipo - nome do clima

        bloqueante - Indica se o clima é bloqueante.

        probabilidade - Indica a probabilidade do clima ocorrer.
        """
        self.id = id
        self.tipo = tipo
        self.bloqueante = bloqueante
        self.probabilidade = probabilidade

    def __eq__(self, other):
        """Compara os objetos Clima apenas pelo tipo"""
        if isinstance(other, Clima):
            return self.tipo == other.tipo
        return False

    def isBlocking(self) -> bool:
        """
        Verifica se o clima está bloqueando. Retorna True se a probabilidade for 100 ou bloquante for True.
        """

        return self.probabilidade == 100 or self.bloqueante

    # Métodos para setar e obter o ID
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    # Métodos para setar e obter o Tipo
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
    
    # Métodos para setar e obter Bloquante
    def setBloqueante(self, bloqueante):
        self.bloqueante = bloqueante

    def getBloqueante(self):
        return self.bloqueante

    # Métodos para setar e obter o Probabilidade
    def setProbabilidade(self, probabilidade):
        self.probabilidade = probabilidade

    def getProbabilidade(self):
        return self.probabilidade
    

class Neve(Clima):
    def __init__(self, id, probabilidade = 0):
        super().__init__(id, tipo="Neve", bloqueante=True, probabilidade=probabilidade)


class Chuva(Clima):
    def __init__(self, id, probabilidade = 0):
        super().__init__(id, tipo="Chuva", bloqueante=False, probabilidade=probabilidade)


class Ensolarado(Clima):
    def __init__(self, id, probabilidade = 0):
        super().__init__(id, tipo="Ensolarado", bloqueante=False, probabilidade=probabilidade)

