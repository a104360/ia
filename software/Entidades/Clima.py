class Clima:
    def __init__(self, tipo, id = -1, probabilidade = 0):
        """
        Classe base para representar diferentes tipos de clima.
        
        id - valor único de cada clima

        tipo - nome do clima

        probabilidade - Indica a probabilidade do clima ocorrer. ([0,10])
        """
        self.id = id
        self.tipo = tipo
        self.probabilidade = probabilidade

    def __eq__(self, other):
        """Compara os objetos Clima apenas pelo tipo"""
        if isinstance(other, Clima):
            return self.tipo == other.tipo
        return False

    def isBlocking(self) -> bool:
        """
        Verifica se o clima é 10. Retorna True se a probabilidade for 10 e transforma este valor em 0.
        Se probabilidade for 10, bloqueia a zona 1 iteracao
        """
        if self.probabilidade == 10:
            self.probabilidade = 0
            return True
        return False

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

    # Métodos para setar e obter o Probabilidade
    def setProbabilidade(self, probabilidade):
        self.probabilidade = probabilidade

    def getProbabilidade(self):
        return self.probabilidade
    

class Neve(Clima):
    def __init__(self, id, probabilidade = 0):
        super().__init__(id, tipo="Neve", probabilidade=probabilidade)


class Chuva(Clima):
    def __init__(self, id, probabilidade = 0):
        super().__init__(id, tipo="Chuva", probabilidade=probabilidade)


class Ensolarado(Clima):
    def __init__(self, id, probabilidade = 0):
        super().__init__(id, tipo="Ensolarado", probabilidade=probabilidade)

