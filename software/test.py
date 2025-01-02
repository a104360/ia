from Entidades.veiculos import Veiculo
from Entidades.veiculos import Camiao
from Entidades.veiculos import Aviao
from Entidades.veiculos import Barco
from Entidades.veiculos import Carro
from Entidades.veiculos import Helicoptero
import json
import random

mapa = list()

def roleta():
    cart = list()
    choices = ["Gorro","Bruffen","Leite","Arroz"]
    for i in range(4):
        slot = random.choice(choices)
        choices.remove(slot)
        if slot == "Gorro":
            cart.append(Veiculo.Bem.Gorro(i,random.randint(10,20)).to_dict())
        if slot == "Bruffen":
            cart.append(Veiculo.Bem.Bruffen(i,random.randint(10,20)).to_dict())
        if slot == "Leite":
            cart.append(Veiculo.Bem.Leite(i,random.randint(10,20)).to_dict())
        if slot == "Arroz":
            cart.append(Veiculo.Bem.Arroz(i,random.randint(10,20)).to_dict())
    return cart
    # 10 - 20
    # 50 - 70

with open("ConfigFiles/mapa.json","r") as f:
    mapa = json.load(f)
    for z in mapa:
        z["necessidades"] = roleta()

with open("ConfigFiles/mapa.json","w") as f:
    json.dump(mapa,f,indent=5)


#file = open("./ConfigFiles/frota.json","r")
#
#stringV = json.load(file)
#
#frota = dict()
#
#for v in stringV:
#    id = v["id"]
#    name = v["name"]
#    capacidade = v["capacidade"]
#    combustivel = v["combustivel"]
#    if v["tipo"] == Camiao.Camiao().getType():
#        frota[id] = Camiao.Camiao(capacidade,combustivel,name,id)
#    if v["tipo"] == Carro.Carro().getType():
#        frota[id] = Carro.Carro(capacidade,combustivel,name,id)
#    if v["tipo"] == Helicoptero.Helicoptero().getType():
#        frota[id] = Helicoptero.Helicoptero(capacidade,combustivel,name,id)
#    if v["tipo"] == Aviao.Aviao().getType():
#        frota[id] = Aviao.Aviao(capacidade,combustivel,name,id)
#    if v["tipo"] == Barco.Barco().getType():
#        frota[id] = Barco.Barco(capacidade,combustivel,name,id)
#
#for v in frota.values():
#    print(v.__str__())
#
#
#
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