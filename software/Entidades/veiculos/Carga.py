from Bem import Bem
from typing import List

class Carga:
    def __init__(self, maxCarga, cargaAtual = 0, bens = {}):
        """
            maxCarga - a capacidade máxima da carga

            cargaAtual - carga atual

            bens - dicionário para armazenar bens (chave: id, valor: objeto Bem)
        """
        self.maxCarga = maxCarga
        self.cargaAtual = cargaAtual
        self.bens: List[int, Bem] = bens

    def __str__(self):
        bens_info = "\n".join(bem.__str__() for bem in self.bens.values())
        return f"Capacidade Máxima: {self.maxCarga}kg\nCarga Atual: {self.cargaAtual}kg\nBens:\n{bens_info}"

    def restock(self, bens: List[Bem]):
        """
        Adiciona uma lista de objetos do tipo 'Bem' à carga.
        Se o bem já existir, atualiza seu peso somando ao peso atual,
        respeitando o limite de capacidade.
        
        bens - lista de objetos do tipo 'Bem'
        """
        for bem in bens:
            if bem.id in self.bens:
                # Bem já existe, tenta atualizar o peso
                peso_novo = self.bens[bem.id].peso + bem.peso
                if self.cargaAtual - self.bens[bem.id].peso + peso_novo <= self.maxCarga:
                    self.cargaAtual += bem.peso  # Apenas adiciona o incremento de peso
                    self.bens[bem.id].peso = peso_novo

            else:
                # Bem não existe, tenta adicionar
                if self.cargaAtual + bem.peso <= self.maxCarga:
                    self.bens[bem.id] = bem
                    self.cargaAtual += bem.peso

    def distribute(self, bens: list[Bem]):
        """
        Remove uma lista de objetos do tipo 'Bem' da carga.
        
        bens - lista de objetos do tipo 'Bem' a serem removidos.
        """
        for bem in bens:
            if bem.id in self.bens:
                # Remove o bem pelo ID
                bem_removido = self.bens.pop(bem.id)
                self.cargaAtual -= bem_removido.peso


    def getBemById(self, id):
        """
        Retorna um objeto 'Bem' pelo ID, se existir.
        """
        return self.bens.get(id, None)

    def removeBemById(self, id):
        """
        Remove um objeto 'Bem' da carga pelo ID, se existir.
        """
        bem = self.bens.pop(id, None)
        if bem:
            self.cargaAtual -= bem.peso

    def getCargaAtual(self):
        """
        Retorna a carga atual.
        """
        return self.cargaAtual

    def getMaxCarga(self):
        """
        Retorna a capacidade máxima da carga.
        """
        return self.maxCarga

    def getCargaDisponivel(self):
        """
        Retorna a capacidade de carga disponivel.
        """
        return self.maxCarga - self.cargaAtual
    
    def getBens(self):
        """
        Retorna a lista de bens armazenados na carga.
        """
        return list(self.bens.values())
