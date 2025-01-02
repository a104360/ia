# Classe grafo para representaçao de grafos,
from collections import deque
import math
from queue import Queue
import random

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem
from Entidades.Zona import Zona
from Entidades.veiculos import Veiculo
from Entidades.veiculos import Bem


# Constructor
# Methods for adding edges
# Methods for removing edges
# Methods for searching a graph
# BFS, DFS, A*, Greedy





class Graph:
    def __init__(self, directed=False,zonas : list[Zona] = []):
        self.m_zonas : list[Zona] = zonas  
        self.m_directed = directed
        self.m_graph = {}  
        self.m_h = {}
        self.counter = 0

    #############
    #    escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "zona" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    #############
    # funcao para ver se a zona tem alguma zona não bloqueada que leve a si, para que n existam bloqueios no randotron
    #############


    #############
    #    modifica valores para outros de maneira semi-random
    #############
    def randotron(self):
        """
        Para cada zona em m_zonas, muda alguns dos seus parametros para refletir a vida real
        """
        for zona in self.m_zonas:
            acessos = [random.randint(0, 1) for _ in range(3)] # lista com 3 valores random 0 ou 1
            zona.setAcessibilidade(acessos)

            populacao = random.randint(0, 100)
            prioritou = False
            gravidade = zona.getGravidade()
            densidade = zona.getDensidade()
            if populacao < 10 and densidade != 1:
                zona.setDensidade(densidade - 1)
                if populacao == 0 and gravidade != 0:
                    prioritou = True
                    zona.setGravidade(gravidade - 1)

            elif populacao > 90 and densidade != 5:
                zona.setDensidade(densidade + 1)
                if populacao == 100 and gravidade != 5:
                    prioritou = True
                    zona.setGravidade(gravidade + 1)

            #num rando de 1 a 100 e se prioritou for false aumentar a gravidade se ...

            iteracao = zona.getIteracoes()
            #3 num random para os clima de 0 a 100, se for 100 a prob eles sao bloq por 1 ronda e a prob passa a -5, se a prob for neg incrementar e ...
            #algo para aumentar os produtos, como se a densidade aumentar e a gravidade, depois guardar a localizacao dos veiculos e algo para fazer descarga e assim
            return

    ################################
    #   encontrar regiao pelo nome
    ################################

    def get_zona_by_name(self, name):
        search_zona = Zona(name)
        for zona in self.m_zonas:
            if zona == search_zona:
                return zona
          
        return None

    ############################
    #   imprimir arestas
    ############################

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for regiao in lista:
            for (regiao2, custo) in self.m_graph[regiao]:
                listaA = listaA + regiao + " ->" + regiao2 + " custo:" + str(custo) + "\n"
        return listaA

    ######################
    #   adicionar   aresta no grafo
    ######################

    def add_edge(self, zona1, zona2, distance):
        n1 = Zona(zona1)
        n2 = Zona(zona2)
        if (n1 not in self.m_zonas):
            n1_id = len(self.m_zonas)  # numeração sequencial
            n1.setId(n1_id)
            self.m_zonas.append(n1)
            self.m_graph[zona1] = []
        else:
            n1 = self.get_zona_by_name(zona1)

        if (n2 not in self.m_zonas):
            n2_id = len(self.m_zonas)  # numeração sequencial
            n2.setId(n2_id)
            self.m_zonas.append(n2)
            self.m_graph[zona2] = []
        else:
            n2 = self.get_zona_by_name(zona2)

        self.m_graph[zona1].append((zona2, distance)) 

        if not self.m_directed:
            self.m_graph[zona2].append((zona1, distance))

    #############################
    # devolver regiaos
    #############################

    def getZonas(self):
        return self.m_zonas

    #######################
    #    devolver o custo de uma aresta
    #######################

    def get_arc_cost(self, zona1, zona2):
        custoT = math.inf
        a = self.m_graph[zona1]  # lista de arestas para aquele regiao
        for (regiao, custo) in a:
            if regiao == zona2:
                custoT = custo

        return custoT

    ###############################
    #  dado um caminho calcula o seu custo
    ###############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de regiaos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo
    

    #################################################
    #  Proxima Zona a escolher Procura não Informada
    #################################################
    def proximaZona(self, veiculo : Veiculo.Veiculo ):  #Devolve o melhor visinho para a zona atual
        zonas : list[Zona] = self.getNeighbours()
    
        proximaZona = None
        maiorPrioridade = 0  # Define prioridade mínima inicial

        listZonas : list[Zona] = []
        tipo = veiculo.getType()

        #ACESSIBILIDADE TIPO VEICULO
        for z in zonas: #verifica para todos os visinhos os que são acessiveis e adiciona a uma lista
            if tipo == "terra":
                if z.isAcessivelTerrestre():
                    listZonas.append(z)
            if tipo == "ar":
                if z.isAcessivelAerea():
                    listZonas.append(z)
            else:
                if z.isAcessivelMaritima():
                    listZonas.append(z)
        
        if listZonas == None: #se estiver vazia o veiculo já não pode ir para mais lugar nenhum
            return None
        

        bensVeiculo : list[Bem.Bem] = veiculo.getBensAvailable
        encontrou = False

        #BENS NECESSARIOS
        for z1 in listZonas: #verifica se os vizinhos precisam de bens que o veiculo leva caso não precisem remove da lista
            bens : list[Bem.Bem]  = z1.getNecessidades()

            for b in bens: #vai à lista de bens da Zona e percorre todos
                if encontrou == True: #se tiver encontrado um bem em comum para
                    break
                for bV in bensVeiculo: #vai à lista de bens do veiculo e percorre todos
                    if b.getId == bV.getId: #se encontrar um bem em comum com a zona sai do ciclo mudando encontrou para True
                        encontrou = True
                        break
            
            if encontrou == False: #se não tive encontrado remove essa zona da lista
                listZonas.remove(z1)
            
            if encontrou == True: #volta o encontrou para False depois de ter verificado uma Zona
                encontrou = False


        if listZonas == None: #se estiver vazia o veiculo já não pode ir para mais lugar nenhum
            return None

        

        return proximaZona


    ####################################################################################
    #  Procura DFS  -- depth first search
    ####################################################################################
    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            return (path,custoT)
        for(adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if (resultado) is not None:
                    return resultado
    
    ######################################################
    # Procura BFS  -- pesquisa em largura
    ######################################################

    def procura_BFS(self,start,end):
        if start == end:
            return [start]
        
        visited = set([start])
        q = deque([start])

        path = {start:([start],0)}
        print(path)
        
        cost = 0

        while q:
            zona = q.popleft()

            for (adjacent,zonaCost) in self.m_graph[zona]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    q.append(adjacent)

                    path[adjacent] = path[zona] + (adjacent,zonaCost)
                    
                    if adjacent == end:
                        finalPath = path[start]

                        for a in path[adjacent]:
                            if a.__class__ == int:
                                cost += a
                            else:
                                finalPath[0].append(a)
                        return (finalPath[0],cost)

            
    ##############################
    # funçãop  getneighbours, devolve vizinhos de um nó
    ##############################

    def getNeighbours(self, regiao):
        lista = []
        for (adjacente, peso) in self.m_graph[regiao]:
            lista.append((adjacente, peso))
        return lista

    
    ###########################
    # desenha grafo  modo grafico
    ###########################

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_zonas
        lista_a = []
        g = nx.Graph()
        for regiao in lista_v:
            n = regiao.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, distance=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True)
        labels = nx.get_edge_attributes(g, 'distance')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    ####################################
    #    add_heuristica   -> define heuristica para cada regiao 1 por defeito....
    ####################################

    def add_heuristica(self, n, estima):
        n1 = Zona(n)
        if n1 in self.m_zonas:
            self.m_h[n] = estima



    ##########################################
    #    A* - greedy mas somas distancia
    ##########################################
                
    def procura_aStar(self, start, end):
        # tuplo de lista dos nomes com custo do caminho pretendido
        path = ([start], 0)
        #set com nomes dos regiaos
        visited = {start}

        q = deque([start])
        custoPath = {start:([start],0)}

        # String nextZona
        currentZona = start 
        
        # vizinhos mantém as ligações ao regiao que estamos a analisar
        vizinhos = self.getNeighbours(currentZona)

        while vizinhos:
            visited.add(currentZona)
            # heuristics guarda o nome dos regiaos e a sua heuristica
            heuristics = []

            for (zona, custo) in vizinhos:
                if zona not in visited:

                    q.append(zona)
                    lista = custoPath[currentZona][0].copy()
                    lista.append(zona)
                    custoZona = custoPath[currentZona][1]
                    custoPath[zona] = (lista,custoZona+custo)

                    heuristics.append((zona,self.getH(zona) + custoPath[zona][1]))
            
            heuristics.sort(key=lambda x: x[1])
            
            # nextZona = (nome,heuristic)
            nextZona = heuristics[0]

            changePath = path[0]
            changePath.append(nextZona[0])
            changeCost = path[1]
            changeCost += self.get_arc_cost(currentZona,nextZona[0])
            path = (changePath,changeCost)

            #print(path)

            if nextZona[0] == end:
                return path

            
            currentZona = nextZona[0]
            vizinhos = self.getNeighbours(nextZona[0])

        return ([],-1)
        

    ####################################
    # devolve heuristica do regiao
    ####################################

    def getH(self, regiao):
        if regiao not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[regiao])


    ##########################################
    #   Greedy - so heuristica da vida
    ##########################################

    def greedy(self,start,end):
        # tuplo de lista dos nomes com custo do caminho pretendido
        path = ([start],0)
        
        #set com nomes dos regiaos
        visited = {start}

        # String nextZona
        currentZona = start 
        
        # vizinhos mantém as ligações ao regiao que estamos a analisar
        vizinhos = self.getNeighbours(currentZona)

        while vizinhos:
            visited.add(currentZona)
            # heuristics guarda o nome dos regiaos e a sua heuristica
            heuristics = []

            for zona in vizinhos:
                if zona[0] not in visited:
                    heuristics.append((zona[0],self.getH(zona[0])))
            
            heuristics.sort(key=lambda x: x[1])
            
            # nextZona = (nome,heuristic)
            nextZona = heuristics[0]

            changePath = path[0]
            changePath.append(nextZona[0])
            changeCost = path[1]
            changeCost += self.get_arc_cost(currentZona,nextZona[0])
            path = (changePath,changeCost)

            #print(path)

            if nextZona[0] == end:
                return path

            
            currentZona = nextZona[0]
            vizinhos = self.getNeighbours(nextZona[0])

        return ([],-1)

    
    