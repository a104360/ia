from Entidades import Zona
from Entidades import Empresa

com = Empresa.Empresa()

com.loadFrota("ConfigFiles/frota.json")

print(com.frota)


