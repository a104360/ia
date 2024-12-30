from veiculos.Bem import Bem
from typing import Dict

class Zona:
    def __init__(self, name, acessibilidade, clima, id=-1, gravidade=0, densidade=0, necessidades={}):     
        """
            id - valor único de cada Zona

            name - nome da Zona

            gravidade - gravidade do problema

            densidade - densidade populacional

            prioridade - o quão prioritária esta Zona é, sendo 1 o que menor prioridade tem

            acessibilidade - acessibilidade marítima, terrestre ou aérea

            clima - clima (chuva, sol, etc)

            necessidades - dicionário de Bens que a Zona necessita
        """
        self.id = id
        self.name = name
        self.gravidade = gravidade
        self.densidade = densidade
        self.prioridade = self.calculatePrioridade(gravidade, densidade)
        self.acessibilidade = acessibilidade
        self.clima = clima
        self.necessidades: Dict[int, Bem] = necessidades

    def calculatePrioridade(self, gravidade, densidade):
        """Calcula a prioridade com base na gravidade e densidade."""
        return gravidade * densidade

    def __str__(self):
        return f"Zona : {self.name}"

    def __repr__(self):
        return f"Zona : {self.name}"

    # Métodos para 'id'
    def setId(self, id: int):
        """Define o ID da Zona."""
        self.id = id

    def getId(self) -> int:
        """Retorna o ID da Zona."""
        return self.id

    # Métodos para 'name'
    def setName(self, name: str):
        """Define o nome da Zona."""
        self.name = name

    def getName(self) -> str:
        """Retorna o nome da Zona."""
        return self.name

    # Métodos para 'gravidade'
    def setGravidade(self, gravidade: int):
        """Define a gravidade da Zona."""
        self.gravidade = gravidade
        self.prioridade = self.calculatePrioridade(self.gravidade, self.densidade)

    def getGravidade(self) -> int:
        """Retorna a gravidade da Zona."""
        return self.gravidade

    # Métodos para 'densidade'
    def setDensidade(self, densidade: int):
        """Define a densidade populacional da Zona."""
        self.densidade = densidade
        self.prioridade = self.calculatePrioridade(self.gravidade, self.densidade)

    def getDensidade(self) -> int:
        """Retorna a densidade populacional da Zona."""
        return self.densidade

    # Métodos para 'prioridade'
    def getPrioridade(self) -> int:
        """Retorna a prioridade da Zona."""
        return self.prioridade

    # Métodos para 'acessibilidade'
    def setAcessibilidade(self, acessibilidade: str):
        """Define a acessibilidade da Zona."""
        self.acessibilidade = acessibilidade

    def getAcessibilidade(self) -> str:
        """Retorna a acessibilidade da Zona."""
        return self.acessibilidade

    # Métodos para 'clima'
    def setClima(self, clima: str):
        """Define o clima da Zona."""
        self.clima = clima

    def getClima(self) -> str:
        """Retorna o clima da Zona."""
        return self.clima

    # Métodos para 'necessidades'
    def setNecessidades(self, necessidades: Dict[int, Bem]):
        """Define as necessidades da Zona."""
        self.necessidades = necessidades

    def getNecessidades(self):
        """Retorna as necessidades da Zona."""
        return self.necessidades

    def addNecessidade(self, bem: Bem):
        """Adiciona um Bem às necessidades da Zona."""
        self.necessidades[bem.id] = bem

    def removeNecessidade(self, bem_id: int):
        """Remove um Bem das necessidades da Zona pelo ID."""
        if bem_id in self.necessidades:
            self.necessidades.pop(bem_id)
