import Veiculo
import Camiao
import Aviao
import Barco
import Carro
import Helicoptero
import json

file = open("../../ConfigFiles/frota.json","r")

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

for v in frota.values():
    print(v.__str__())



#print(frota)
#
#c = Camiao.Camiao()
#
#if isinstance(c,Veiculo.Veiculo):
#    print("Camiao e um veiculo")
#
#print(c.__str__())
#
#
#c = Aviao.Aviao()
#
#if isinstance(c,Veiculo.Veiculo):
#    print("Aviao e um veiculo")
#
#
#print(c.__str__())