# Classe grafo para representaçao de grafos,
from collections import deque
import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem
from Grafo import Node


# Constructor
# Methods for adding edges
# Methods for removing edges
# Methods for searching a graph
# BFS, DFS, A*, Greedy





class Graph:
    def __init__(self, directed=False):
        self.m_nodes = []  
        self.m_directed = directed
        self.m_graph = {}  
        self.m_h = {}  

    #############
    #    escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    ################################
    #   encontrar regiao pelo nome
    ################################

    def get_node_by_name(self, name):
        search_node = Node.Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
          
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

    def add_edge(self, node1, node2, weight):
        n1 = Node.Node(node1)
        n2 = Node.Node(node2)
        if (n1 not in self.m_nodes):
            n1_id = len(self.m_nodes)  # numeração sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []
        else:
            n1 = self.get_node_by_name(node1)

        if (n2 not in self.m_nodes):
            n2_id = len(self.m_nodes)  # numeração sequencial
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []
        else:
            n2 = self.get_node_by_name(node2)

        self.m_graph[node1].append((node2, weight)) 

        if not self.m_directed:
            self.m_graph[node2].append((node1, weight))

    #############################
    # devolver regiaos
    #############################

    def getNodes(self):
        return self.m_nodes

    #######################
    #    devolver o custo de uma aresta
    #######################

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele regiao
        for (regiao, custo) in a:
            if regiao == node2:
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

    ####################################################################################
    #     procura DFS  -- depth first search
    ####################################################################################
    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            return custoT
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
            node = q.popleft()

            for (adjacent,nodeCost) in self.m_graph[node]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    q.append(adjacent)

                    path[adjacent] = path[node] + (adjacent,nodeCost)
                    
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
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for regiao in lista_v:
            n = regiao.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    ####################################
    #    add_heuristica   -> define heuristica para cada regiao 1 por defeito....
    ####################################

    def add_heuristica(self, n, estima):
        n1 = Node.Node(n)
        if n1 in self.m_nodes:
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

        # String nextNode
        currentNode = start 
        
        # vizinhos mantém as ligações ao regiao que estamos a analisar
        vizinhos = self.getNeighbours(currentNode)

        while vizinhos:
            visited.add(currentNode)
            # heuristics guarda o nome dos regiaos e a sua heuristica
            heuristics = []

            for (node, custo) in vizinhos:
                if node not in visited:

                    q.append(node)
                    lista = custoPath[currentNode][0].copy()
                    lista.append(node)
                    custoNode = custoPath[currentNode][1]
                    custoPath[node] = (lista,custoNode+custo)

                    heuristics.append((node,self.getH(node) + custoPath[node][1]))
            
            heuristics.sort(key=lambda x: x[1])
            
            # nextNode = (nome,heuristic)
            nextNode = heuristics[0]

            changePath = path[0]
            changePath.append(nextNode[0])
            changeCost = path[1]
            changeCost += self.get_arc_cost(currentNode,nextNode[0])
            path = (changePath,changeCost)

            #print(path)

            if nextNode[0] == end:
                return path

            
            currentNode = nextNode[0]
            vizinhos = self.getNeighbours(nextNode[0])

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

        # String nextNode
        currentNode = start 
        
        # vizinhos mantém as ligações ao regiao que estamos a analisar
        vizinhos = self.getNeighbours(currentNode)

        while vizinhos:
            visited.add(currentNode)
            # heuristics guarda o nome dos regiaos e a sua heuristica
            heuristics = []

            for node in vizinhos:
                if node[0] not in visited:
                    heuristics.append((node[0],self.getH(node[0])))
            
            heuristics.sort(key=lambda x: x[1])
            
            # nextNode = (nome,heuristic)
            nextNode = heuristics[0]

            changePath = path[0]
            changePath.append(nextNode[0])
            changeCost = path[1]
            changeCost += self.get_arc_cost(currentNode,nextNode[0])
            path = (changePath,changeCost)

            #print(path)

            if nextNode[0] == end:
                return path

            
            currentNode = nextNode[0]
            vizinhos = self.getNeighbours(nextNode[0])

        return ([],-1)

    




