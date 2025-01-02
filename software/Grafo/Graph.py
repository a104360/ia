# Classe grafo para representaçao de grafos,
from collections import deque
import math
from queue import Queue
import random

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem
from Entidades.Zona import Zona
from Entidades.Clima import Clima
from Entidades.veiculos.Veiculo import Veiculo
from Entidades.veiculos.Bem import Bem


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

    def movimento(self, veiculo : Veiculo, zona : Zona, tipo):
        """
        Para uma Zona e um Veiculo, faz uma ação, desde encher o tanque, deixar carga ou movimentar
        """
        if tipo == 0: #passar pela zona
            return
        if tipo == 1: #abastecer na Zona
            return
        if tipo == 2: #airdrop na Zona
            return

    #############
    #    modifica valores para uma Zona de maneira semi-random
    #############
    def zonotron(self, zona : Zona):
        """
        Para uma Zona, muda alguns dos seus parametros para refletir a vida real, se as suas iteracoes 
        for superior à sua janela então a zona ficará permanenentemente ploqueada
        """

        if zona.isBloqueado(): return

        acessos = [bool(random.randint(0, 1)) for _ in range(3)] # lista com 3 valores random True ou False 
        zona.setAcessibilidade(acessos)

        clima : Clima = zona.getClima() # clima da Zona
        prbClima = clima.getProbabilidade() # prob do clima
        newClima = random.randint(prbClima, 10) # entre a prob e 10
        clima.setProbabilidade(newClima) # nova prob, se 10 aumenta a iteracao e volta prob a 0
        zona.setClima(clima)
        iteracao = zona.getIteracoes()
        zona.setIteracoes(iteracao + 1)
        zona.shouldBeBlocked() # ve se iteracao e maior que a janela

    ################################
    #   encontrar zona pelo nome
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
        for zona in lista:
            for (zona2, custo) in self.m_graph[zona]:
                listaA = listaA + zona + " ->" + zona2 + " custo:" + str(custo) + "\n"
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
    # devolver zonas
    #############################

    def getZonas(self):
        return self.m_zonas

    #######################
    #    devolver o custo de uma aresta
    #######################

    def get_arc_cost(self, zona1, zona2):
        custoT = math.inf
        a = self.m_graph[zona1]  # lista de arestas para aquele zona
        for (zona, custo) in a:
            if zona == zona2:
                custoT = custo

        return custoT

    ###############################
    #  dado um caminho calcula o seu custo
    ###############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de zonas
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo
    
    #################################################
    #  Proxima Zona a escolher Procura Informada
    #################################################
    def proximaZona(self, veiculo : Veiculo.Veiculo, currentZona : Zona):  #Devolve o melhor visinho para a zona atual
        zonas = self.getNeighbours(currentZona)
    
        proximaZona = None

        listZonas : list[Zona] = []
        tipo = veiculo.getType

        #ACESSIBILIDADE TIPO VEICULO
        for z, distancia in zonas: #verifica para todos os visinhos os que são acessiveis e adiciona a uma lista
            if veiculo.getAutonomy() < distancia:
                continue
            if z.isBloqueado() == False: #zona não esta bloqueada
                if tipo == "terra":
                    if z.isAcessivelTerrestre():
                        listZonas.append(z)
                if tipo == "ar":
                    if z.isAcessivelAerea():
                        listZonas.append(z)
                if tipo == "agua":
                    if z.isAcessivelMaritima():
                        listZonas.append(z)
        
        if len(listZonas) == 0: #se estiver vazia o veiculo já não pode ir para mais lugar nenhum
            return None

        bensVeiculo : list[Bem.Bem] = veiculo.getBensAvailable()
        encontrou = False

        listZonasSemNecessidade : list[Zona] = []
        #BENS NECESSARIOS
        for z1 in listZonas: #verifica se os vizinhos precisam de bens que o veiculo leva caso não precisem remove da lista
            bens : list[Bem.Bem]  = z1.getNecessidades()

            for b in bens: #vai à lista de bens da Zona e percorre todos
                if encontrou == True: #se tiver encontrado um bem em comum para
                    break
                for bV in bensVeiculo: #vai à lista de bens do veiculo e percorre todos
                    if b == bV: #se encontrar um bem em comum com a zona sai do ciclo mudando encontrou para True
                        encontrou = True
                        break
            
            if encontrou == False: #se não tive encontrado remove essa zona da lista
                listZonas.remove(z1)
                listZonasSemNecessidade.append(z1)
            
            if encontrou == True: #volta o encontrou para False depois de ter verificado uma Zona
                encontrou = False


        if len(listZonas) == 0: #se estiver vazia o veiculo recebe uma das zonas para onde pode ir sem alimentos
            listPrio : list[Zona] = []
            maiorPrio = 0
            for zPrio in listZonasSemNecessidade: # ve a maior prioridade
                if zPrio.getPrioridade() > maiorPrio :
                    maiorPrio = zPrio.getPrioridade()
            
            for zAddMostPrio in listZonasSemNecessidade: # guarda os com maior prio numa lista
                if zAddMostPrio.getPrioridade() == maiorPrio :
                    listPrio.append(zAddMostPrio)

            if listPrio.count() <= 1: # retorna se so houver 1 com maior prio ou a lista for vazia
                return listPrio[0]
            else: # se existirem mais de uma zona vai se ver a que possuir menor janela
                menorJanela = math.inf
                for lP in listPrio:
                    x = lP.getJanela() - lP.getIteracoes()
                    if(x < menorJanela):
                        proximaZona = lP
                        menorJanela = x

            
        return proximaZona

    ################################################
    #   Verifica se pode ir para o adjacente
    ################################################

    def verificaAdjacente(self, adjacente : Zona,veiculo : Veiculo):
        tipo = veiculo.getType

        if adjacente.isBloqueado() == True: #zona está bloqueada
            return False
        #ACESSIBILIDADE TIPO VEICULO
        if tipo == "terra":
            if adjacente.isAcessivelTerrestre():
                return True
        elif tipo == "ar":
            if adjacente.isAcessivelAerea():
                return True
        elif tipo == "agua":
            if adjacente.isAcessivelMaritima():
                return True
        else:
            return False



    ####################################################################################
    #  Procura DFS  -- depth first search
    ####################################################################################
    def procura_DFS(self, start, end, veiculo : Veiculo.Veiculo ,path=[], visited=set()):
        path.append(start)
        visited.add(start)
        
        bens : list[Bem.Bem] = veiculo.getBensAvailable
        if start == end or len(bens) <= 0:
            custoT = self.calcula_custo(path)
            return (path,custoT)
        
        for(adjacente, distancia) in self.m_graph[start]:
            if adjacente not in visited and self.verificaAdjacente(adjacente,veiculo) :
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

    def getNeighbours(self, zona):
        lista = []
        for (adjacente, distancia) in self.m_graph[zona]:
            lista.append((adjacente, distancia))
        return lista

    
    ###########################
    # desenha grafo  modo grafico
    ###########################

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_zonas
        lista_a = []
        g = nx.Graph()
        for zona in lista_v:
            n = zona.getName()
            g.add_node(n)
            for (adjacente, distancia) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, distance=distancia)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True)
        labels = nx.get_edge_attributes(g, 'distance')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    ####################################
    #    add_heuristica   -> define heuristica para cada zona 1 por defeito....
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
        #set com nomes dos zonas
        visited = {start}

        q = deque([start])
        custoPath = {start:([start],0)}

        # String nextZona
        currentZona = start 
        
        # vizinhos mantém as ligações ao zona que estamos a analisar
        vizinhos = self.getNeighbours(currentZona)

        while vizinhos:
            visited.add(currentZona)
            # heuristics guarda o nome dos zonas e a sua heuristica
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
    # devolve heuristica do zona
    ####################################

    def getH(self, zona):
        if zona not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[zona])


    ##########################################
    #   Greedy - so heuristica da vida
    ##########################################

    def greedy(self,start,end):
        # tuplo de lista dos nomes com custo do caminho pretendido
        path = ([start],0)
        
        #set com nomes dos zonas
        visited = {start}

        # String nextZona
        currentZona = start 
        
        # vizinhos mantém as ligações ao zona que estamos a analisar
        vizinhos = self.getNeighbours(currentZona)

        while vizinhos:
            visited.add(currentZona)
            # heuristics guarda o nome dos zonas e a sua heuristica
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

    
    