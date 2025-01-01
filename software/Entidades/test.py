import Zona
a = Zona.Zona("Alfama",2020)

print(a)

print(f"Test 1 - {a.calculatePrioridade(a.getGravidade(),a.getDensidade())}")