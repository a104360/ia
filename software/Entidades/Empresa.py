import json
from .veiculos import Camiao
from .veiculos import Carro
from .veiculos import Helicoptero
from .veiculos import Aviao
from .veiculos import Barco
from .veiculos import Veiculo
from . import Zona


class Empresa:
    def __init__(self,tempoTotal):
        self.frota = dict()
        self.posicoesAgentes = dict()
        self.tempoTotal = tempoTotal
        self.tabelaCustos = dict(str,int)
    
    def decisao(self,zonas : list[Zona.Zona],agentes : list[Veiculo.Veiculo]) -> int:
        """
            Função para tomada de decisão a cada iteração
        """
        None

    def runSimulation(self,time = 2880):
        self.tempoTotal = time
        """
            Função responsável por efetuar as alterações do estado.
        """
        None

    def loadFrota(self,filename:str):
        """Loads a map with the vehicles available from a json file"""
        file = open(filename,"r")

        stringV = json.load(file)

        for v in stringV:
            id = v["id"]
            name = v["name"]
            capacidade = v["capacidade"]
            combustivel = v["combustivel"]
            if v["tipo"] == Camiao.Camiao().getType():
                self.frota[id] = Camiao.Camiao(capacidade,combustivel,name,id)
            if v["tipo"] == Carro.Carro().getType():
                self.frota[id] = Carro.Carro(capacidade,combustivel,name,id)
            if v["tipo"] == Helicoptero.Helicoptero().getType():
                self.frota[id] = Helicoptero.Helicoptero(capacidade,combustivel,name,id)
            if v["tipo"] == Aviao.Aviao().getType():
                self.frota[id] = Aviao.Aviao(capacidade,combustivel,name,id)
            if v["tipo"] == Barco.Barco().getType():
                self.frota[id] = Barco.Barco(capacidade,combustivel,name,id)
    #TODO:
    #runsimultation(time:int)
    #setPrioridades