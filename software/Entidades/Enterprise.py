import json
from veiculos import Camiao
from veiculos import Carro
from veiculos import Helicoptero
from veiculos import Aviao
from veiculos import Barco


class Enterprise:
    def __init__(self):
        frota = dict()
        prioridades = list()
    


    def loadFrota(self,filename:str):
        """Loads a map with the vehicles available from a json file"""
        file = open(filename,"r")

        stringV = json.load(file)

        frota = dict()

        for v in stringV:
            id = v["id"]
            name = v["name"]
            capacidade = v["capacidade"]
            combustivel = v["combustivel"]
            if v["tipo"] == Camiao.Camiao().getType():
                frota[id] = Camiao.Camiao(capacidade,combustivel,name,id)
            if v["tipo"] == Carro.Carro().getType():
                frota[id] = Carro.Carro(capacidade,combustivel,name,id)
            if v["tipo"] == Helicoptero.Helicoptero().getType():
                frota[id] = Helicoptero.Helicoptero(capacidade,combustivel,name,id)
            if v["tipo"] == Aviao.Aviao().getType():
                frota[id] = Aviao.Aviao(capacidade,combustivel,name,id)
            if v["tipo"] == Barco.Barco().getType():
                frota[id] = Barco.Barco(capacidade,combustivel,name,id)
    #TODO:
    #runsimultation(time:int)
    #setPrioridades