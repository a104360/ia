class Bem:
    def __init__(self, id, nome, peso, tipo):
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

    def __str__(self):
        return f"ID : {self.id}\nNome : {self.nome}\nPeso : {self.peso}kg\nTipo : {self.limit}\n"

    def getId(self):
        """Returns o id do Bem"""
        return self.id
    
    def getTipo(self):
        """Returns o nome do Bem"""
        return self.nome
    
    def getPeso(self):
        """Returns o peso/custo do Bem"""
        return self.peso
    
    def getTipo(self):
        """Returns o tipo do Bem"""
        return self.tipo