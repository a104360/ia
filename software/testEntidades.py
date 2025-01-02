from Entidades import Zona
from Entidades import Empresa
from Entidades.veiculos import *
import json

import Entidades.veiculos.Carga
import Entidades.veiculos.Combustivel

#com = Empresa.Empresa()
#
#com.loadFrota("ConfigFiles/frota.json")
#
#print(com.frota)

#list = None
#
#with open("ConfigFiles/mapa.json","r") as f:
#    lista = json.load(f)
#
#
#print(lista)

#lista : list[Entidades.veiculos.Veiculo.Veiculo] = list()
#
#
#lista.append(Entidades.veiculos.Helicoptero.Helicoptero(
#    "Helicoptero",
#    0,
#    200,
#    0,
#    [Entidades.veiculos.Bem.Gorro(0,1).to_dict(),Entidades.veiculos.Bem.Leite(1,1).to_dict()],
#    150,
#    1000,
#    100,
#    "ar"
#    ))
#
#lista.append(Entidades.veiculos.Camiao.Camiao(
#    "Camiao",
#    1,
#    300,
#    0,
#    [Entidades.veiculos.Bem.Gorro(0,5).to_dict(),Entidades.veiculos.Bem.Arroz(2,10).to_dict()],
#    200,
#    2000,
#    150,
#    "terra"
#).to_dict())
#
#lista.append(Entidades.veiculos.Carro.Carro(
#    "Carro",
#    2,
#    100,
#    0,
#    [Entidades.veiculos.Bem.Leite(1,2).to_dict(),Entidades.veiculos.Bem.Bruffen(3,1).to_dict()],
#    50,
#    500,
#    50,
#    "terra"
#).to_dict())
#
#lista.append(Entidades.veiculos.Barco.Barco(
#    "Barco",
#    3,
#    400,
#    0,
#    [Entidades.veiculos.Bem.Arroz(2,20).to_dict(),Entidades.veiculos.Bem.Bruffen(3,5).to_dict()],
#    300,
#    5000,
#    200,
#    "mar"
#).to_dict())
#
#temp = lista[0]

#print(lista[0])

#
#with open("ConfigFiles/keep.json","w") as f:
#    #string = json.dumps(lista)
#    json.dump(lista,f,indent=4)

lista = None
with open("ConfigFiles/keep.json", "r") as f:
    lista = json.load(f)



for i in range(len(lista)):
    lista[i] = Entidades.veiculos.Veiculo.Veiculo("",2).from_dict(lista[i])
    #print(lista[i])


print(lista)

#if temp.id == lista[0].id:
#    print("conseguiu carregar")