class Bem:
    def __init__(self, id : int = 1, nome : str = "", peso : int = 0, tipo : str = ""):
        """
            id - valor único de cada bem

            nome - nome do Bem

            peso - indica o peso/custo de ter este produto

            tipo - agua/comida/medicamentos/etc
        """
        self.id = id
        self.nome = nome
        self.peso = peso
        self.tipo = tipo

    def to_dict(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "peso" : self.peso,
            "tipo" : self.tipo
        }
    
    def from_dict(self,dict):
        return Bem(
            dict["id"],
            dict["nome"],
            dict["peso"],
            dict["tipo"],
        )


    def __eq__(self, other):
        """Compara os objetos Bem apenas pelo nome"""
        if isinstance(other, Bem):
            return self.nome == other.nome
        return False
    
    def __str__(self):
        return f"ID : {self.id}\nNome : {self.nome}\nPeso : {self.peso}kg\nTipo : {self.tipo}\n"

    def getId(self):
        """Returns o id do Bem"""
        return self.id
    
    def getNome(self):
        """Returns o nome do Bem"""
        return self.nome
    
    def getPeso(self):
        """Returns o peso/custo do Bem"""
        return self.peso
    
    def getTipo(self):
        """Returns o tipo do Bem"""
        return self.tipo
    
    def setId(self, id : int):
        """muda o id do Bem"""
        self.id = id
    
    def setNome(self, nome : str):
        """muda o nome do Bem"""
        self.nome = nome
    
    def setPeso(self, peso : int):
        """muda o peso/custo do Bem"""
        self.peso = peso
    
    def setTipo(self, tipo : str):
        """muda o tipo do Bem"""
        self.tipo = tipo
    
    def getDistributionTime(self):
        if self.peso > 20: return 1
        else: return 5

class Leite(Bem):
    def __init__(self, id: int, peso: int):
        super().__init__(id, nome = "Leite", peso = peso, tipo = "Liquido")


class Bruffen(Bem):
    def __init__(self, id: int, peso: int):
        super().__init__(id, nome = "Bruffen", peso = peso, tipo = "Medicamento")


class Arroz(Bem):
    def __init__(self, id: int, peso: int):
        super().__init__(id, nome = "Arroz", peso = peso, tipo = "Comida")


class Gorro(Bem):
    def __init__(self, id: int, peso: int):
        super().__init__(id, nome = "Gorro", peso = peso, tipo = "Roupa")