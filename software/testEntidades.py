from Entidades import Zona
from Entidades import Empresa
import json

#com = Empresa.Empresa()
#
#com.loadFrota("ConfigFiles/frota.json")
#
#print(com.frota)

list = None

with open("ConfigFiles/mapa.json","r") as f:
    lista = json.load(f)


print(lista)