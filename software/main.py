from Grafo import Graph
from Entidades.veiculos import Veiculo
from Entidades.veiculos import *
import json
import os


def getVeiculo(lista : list[Veiculo.Veiculo]):
    count = 0
    for l in lista:
        print(str(count) + "-" + l.name)
        count += 1
    choice = input("Qual veiculo pretende->")
    return lista[int(choice)]
    

def loadFrota():
    lista = None
    with open("ConfigFiles/keep.json", "r") as f:
        lista = json.load(f)
    for i in range(len(lista)):
        lista[i] = Entidades.veiculos.Veiculo.Veiculo("",2).from_dict(lista[i])
    return lista

def main():


    frota = loadFrota()

    

    g = Graph.Graph()

    g.add_edge("elvas", "borba", 15)
    g.add_edge("borba", "estremoz", 15)
    g.add_edge("estremoz", "evora", 40)
    g.add_edge("evora", "montemor", 20)
    g.add_edge("montemor", "vendasnovas", 15)
    g.add_edge("vendasnovas", "lisboa", 50)
    g.add_edge("elvas", "arraiolos", 50)
    g.add_edge("arraiolos", "alcacer", 90)
    g.add_edge("alcacer", "palmela", 35)
    g.add_edge("palmela", "almada", 25)
    g.add_edge("palmela", "barreiro", 20)
    g.add_edge("barreiro", "palmela", 20)
    g.add_edge("almada", "lisboa", 15)
    g.add_edge("elvas", "alandroal", 40)
    g.add_edge("alandroal", "redondo", 25)
    g.add_edge("redondo", "monsaraz", 30)
    g.add_edge("monsaraz", "barreiro", 110)
    g.add_edge("barreiro", "baixadabanheira", 5)
    g.add_edge("baixadabanheira", "moita", 5)
    g.add_edge("moita", "alcochete", 15)
    g.add_edge("alcochete", "lisboa", 15)



    saida = -1
    while saida != 0:
        os.system("clear")
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir  regioes de Grafo")
        print("4-Imprimir arestas de Grafo")
        print("5-DFS")
        print("6-Gulosa")
        #print("8-BFS")
        #print("7-A*")
        #print("9-Iniciar")
        print("0-Saír")

        #print(type(g.m_zonas[0]))
        
        try:
            saida = int(input("introduza a sua opcao-> "))
            if saida == 0:
                print("saindo.......")
            elif saida == 1:
                print(g.m_graph)
                l = input("prima enter para continuar")
            elif saida == 2:
                g.desenha()
            elif saida == 3:
                print(g.m_graph.keys())
                l = input("prima enter para continuar")
            elif saida == 4:
                print(g.imprime_aresta())
                l = input("prima enter para continuar")
            elif saida == 5: # DFS
                v = getVeiculo(frota)
                contador = 0
                for gN in g.m_zonas:
                    print(gN.name)
                    contador += 1
                inicio = input("Nome regiao inicial->")
                i = input("Iterações disponíveis (Entre 15 e 25)->")
                i = int(i)
                if i < 15: i = 15
                print(g.procura_DFS(g.get_zona_by_name(inicio),v,i, path=list(), visited=set()))
                l = input("prima enter para continuar")
                print("saindo.......")
                saida = 0
            elif saida == 8:# BFS
                #inicio = input("Regiao inicial->")
                #fim = input("Regiao final->")
                #print(g.procura_BFS(inicio, fim))
                #l = input("prima enter para continuar")
                #print("saindo.......")
                saida = 0
            elif saida == 7: # A*
                #inicio = input("Regiao inicial->")
                #fim = input("Regiao final->")
                #print(g.procura_aStar(inicio, fim))
                #l = input("prima enter para continuar")
                #print("saindo.......")
                saida = 0
            elif saida == 6: # Gulosa
                v = getVeiculo(frota)
                contador = 0
                for gN in g.m_zonas:
                    print(gN.name)
                    contador += 1
                inicio = input("Nome regiao inicial->")
                i = input("Iterações disponíveis (Entre 15 e 25) ->")
                i = int(i)
                if i < 15: i = 15
                print(g.greedy(g.get_zona_by_name(inicio), v, i, path=list(), visited=set()))
                l = input("prima enter para continuar")
                print("saindo.......")
                saida = 0
            elif saida == 9:
                #time = input("Limite de iteracoes->")
                #simular(time)
                #l = input("prima enter para continuar")
                saida = 0
            else:
                print("you didn't add anything")
                l = input("prima enter para continuar")
        except ValueError:
            continue


if __name__ == "__main__":
    main()


def simular(iteracoes : int):
    #INICIALIZAR AS VARIÁVEIS
    #CICLO PARA TRATAR AS ITERAÇÕES
    #APRESENTAR MÉTRICAS
    print(2)


