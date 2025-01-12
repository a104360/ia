# Classe grafo para representaçao de grafos,
from collections import deque
import math
from queue import Queue
import random
import json

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
    def __init__(self, directed=False,zonas = None):
        self.m_zonas = list()
        if zonas != None: self.m_zonas : list[Zona] = zonas
        else: 
            with open("ConfigFiles/mapa.json","r") as f:
                lista = json.load(f)
                for a in lista:
                    self.m_zonas.append(Zona("").from_dict(a))
        #print(self.m_zonas)
        self.m_directed = directed
        self.m_graph : dict[Zona, list[tuple[Zona, int]]] = dict() 
        self.m_h = {}
        self.iter = 0

    #############
    #    escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "zona" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
    def zonaDefiner(self, iteracoes : int):
        """
        Incrementa o numero de iteracoes de todas as Zonas em iteracoes, 
        se iteracoes for 0, então este irá meter as iterações de todas as Zonas a 0
        """
        if iteracoes == 0:
            for m_zona in self.m_zonas:
                m_zona.setIteracoes(0)
        else:
            for m_zona in self.m_zonas:
                if m_zona.getNecessidades() != None or m_zona.isBloqueado() == False:
                    itera = m_zona.getIteracoes()
                    m_zona.setIteracoes(itera + iteracoes)
            
        if iteracoes == 0:
            for m_zona in self.m_zonas:
                m_zona.setIteracoes(0)
        else:
            for m_zona in self.m_zonas:
                if m_zona.getNecessidades() != None or m_zona.isBloqueado() == False:
                    itera = m_zona.getIteracoes()
                    m_zona.setIteracoes(itera + iteracoes)
            

    #############
    #    modifica valores para uma Zona de maneira semi-random
    #############
    def randomZona(self, zona : Zona):
        """
        Para uma Zona, muda alguns dos seus parametros para refletir a vida real, se as suas iteracoes 
        for superior à sua janela então a zona ficará permanenentemente bloqueada
        """

        if zona.isBloqueado(): return

        #acessos = [bool(random.randint(0, 1)) for _ in range(3)] # lista com 3 valores random True ou False 
        #zona.setAcessibilidade(acessos)

        clima : Clima = zona.getClima() # clima da Zona
        prbClima = clima.getProbabilidade() # prob do clima
        newClima = random.randint(prbClima, 10) # entre a prob e 10
        clima.setProbabilidade(newClima) # nova prob
        zona.setClima(clima)
        zona.isGoingToBeBlocked() #se 10 aumenta a iteracao e volta prob a 0
        zona.nextIter()
        zona.shouldBeBlocked() # ve se iteracao e maior que a janela

    def randomZonas(self, zonas : list[Zona]):
        """
        Para uma lista de Zona, muda alguns dos seus parametros para refletir a vida real, se as suas iteracoes 
        for superior à sua janela então a zona ficará permanenentemente bloqueada
        """

        for zona in zonas:
            self.randomZona(zona)

    ################################
    #   encontrar zona pelo nome
    ################################

    def get_zona_by_name(self, name):
        search_zona = name
        for zona in self.m_zonas:
            if zona.getName() == name:
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

        n1 = self.get_zona_by_name(zona1)
        n2 = self.get_zona_by_name(zona2)

        if (n1 not in self.m_zonas):
            n1_id = len(self.m_zonas)  # numeração sequencial
            n1.setId(n1_id)
            self.m_zonas.append(n1)
            self.m_graph[zona1] = []

        if (n2 not in self.m_zonas):
            n2_id = len(self.m_zonas)  # numeração sequencial
            n2.setId(n2_id)
            self.m_zonas.append(n2)
            self.m_graph[zona2] = []
        
        if not self.m_graph.__contains__(zona1) :self.m_graph[zona1] = list()
        self.m_graph[zona1].append((zona2, distance)) 

        if not self.m_directed:
            if not self.m_graph.__contains__(zona2): self.m_graph[zona2] = list()
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
        print(zona1)
        a = self.m_graph[self.get_zona_by_name(zona1)]  # lista de arestas para aquele zona
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

    ################################################
    #   Verifica se pode ir para o adjacente
    ################################################

    def verificaAdjacente(self, adjacente : Zona,veiculo : Veiculo):
        tipo = veiculo.getType()

        #if adjacente.isBloqueado() == True: #zona está bloqueada
        #    return False
        #ACESSIBILIDADE TIPO VEICULO
        if tipo == "terra":
            if adjacente.isAcessivelTerrestre():
                return True
        elif tipo == "ar":
            if adjacente.isAcessivelAerea():
                return True
        elif tipo == "mar":
            if adjacente.isAcessivelMaritima():
                return True
        else:
            return False

    def consomeBens(self, carro : Veiculo, zona : Zona):
        """
            retira das necessidades da zona as presentes no veiculo
        """
        carroBens = carro.getBensAvailable()
        #print(carroBens)
        for bem in carroBens:
            #print(bem)
            pesoAtual = bem.getPeso()
            bem = zona.removeNecessidade(bem)   
            pesoNovo = 0
            if bem : pesoNovo = bem.getPeso()
            pesoAmais = pesoAtual - pesoNovo
            carro.updateCargaAvailable(-pesoAmais)    


    ####################################################################################
    #  Procura DFS  -- depth first search
    ####################################################################################
    def procura_DFS(self, start : Zona, veiculo : Veiculo, iterM,path : list[Zona] = list(), visited:set=set(), visit = False):
        #print(start)
        print(start.name)
        if self.iter > 0:print("Iterações até momento: "+str(self.iter)+"\n")
        self.iter += 1
        path.append(start) #ira repetir a mesma zona caso n tenha como ir para outra momentaneamente
        if visit == False: visited.add(start)
        
        bens : list[Bem] = veiculo.getBensAvailable()
        if len(bens) == 0 or self.iter >= iterM:
            #custoT = self.calcula_custo(path)
            iterCopia = self.iter - 1 #comeca com 1 iteracao a mais
            #self.iter = 0
            #self.zonaDefiner(0)
            return (path, iterCopia)#custoT, iterCopia)
        
        self.consomeBens(veiculo, start) # tirar do veiculo e zona os bens em comum
        start.shouldBeBlocked() # ve se depois de tirar os bens a zona esta safe

        moveOn = True


        for(adjacente, distancia) in self.m_graph[start.getName()]:
            zona = self.get_zona_by_name(adjacente)
            # se ja se esteve lá ou se fez refil
            if zona not in visited or visit:
                # se a zona esta fechada 
                if zona.isBloqueado() == False:
                    # se tem iteracoes para chegar lá
                    if veiculo.getAutonomy() >= distancia:
                        # se o teu tipo de veiculo e permitido
                        if self.verificaAdjacente(zona, veiculo):
                            moveOn = False

                            veiculo.walkedKm(distancia) #instancias usadas para mover
                            self.randomZonas(self.m_zonas)
                            return self.procura_DFS(zona, veiculo,iterM, path, visited, False)

        if moveOn:
            #iterCopia = self.iter - 1 #comeca com 1 iteracao a mais
            #self.iter = 0
            #self.zonaDefiner(0)
            #return (path, iterCopia)
            veiculo.refuel() #refil
            self.zonaDefiner(1)
            return self.procura_DFS(zona, veiculo,iterM, path,visited, True)

            
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
                lista_a.append(lista)
                g.add_edge(n, adjacente, distance=distancia)

        pos = nx.spring_layout(g,iterations=1)
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
        

    ####################################
    # devolve heuristica do zona
    ####################################

    def getH(self, zona):
        if zona not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[zona])


    #################################################
    #  Proxima Zona a escolher Procura Informada
    #################################################
    def proximaZona(self, veiculo : Veiculo, currentZona : Zona, visitados : set = set()):  #Devolve o melhor visinho para a zona atual    
        proximaZona : Zona = None
        finalDis : int = -1

        listZonas : list[tuple[Zona, int]] = []
        tipo = veiculo.getType()

        #Bloqueamento da Zona
        for (zed, distancia) in self.m_graph[currentZona.getName()]: #verifica para todos os visinhos estão bloqueados
            z = self.get_zona_by_name(zed)
            if z.isBloqueado() == False:
                finalDis = 0
                break
        
        if finalDis == -1: return (proximaZona, finalDis)

        #ACESSIBILIDADE TIPO VEICULO
        for (zed, distancia) in self.m_graph[currentZona.getName()]: #verifica para todos os visinhos os que são acessiveis e adiciona a uma lista
            z = self.get_zona_by_name(zed)
            if veiculo.getAutonomy() >= distancia and z not in visitados and z.isBloqueado() == False: #zona não esta bloqueada
                if tipo == "terra":
                    if z.isAcessivelTerrestre():
                        listZonas.append((z, distancia))
                if tipo == "ar":
                    if z.isAcessivelAerea():
                        listZonas.append((z, distancia))
                if tipo == "mar":
                    if z.isAcessivelMaritima():
                        listZonas.append((z, distancia))
        
        if len(listZonas) == 0: #se estiver vazia o veiculo já não pode ir para mais lugar nenhum
            return (None, 0)

        bensVeiculo : list[Bem] = veiculo.getBensAvailable()
        encontrou = False

        listZonasSemNecessidade : list[tuple[Zona, int]] = []
        #BENS NECESSARIOS
        for (z2, distancia2) in listZonas: #verifica se os vizinhos precisam de bens que o veiculo leva caso não precisem remove da lista
            bens : list[Bem]  = z2.getNecessidades()

            for bV in bensVeiculo: #vai à lista de bens do veiculo e percorre todos
                if bV in bens: #se encontrar um bem em comum com a zona sai do ciclo mudando encontrou para True
                    encontrou = True
                    break
            
            if encontrou == False: #se não tive encontrado remove essa zona da lista
                listZonas.remove((z2, distancia2))
                listZonasSemNecessidade.append((z2, distancia2))
            
            if encontrou == True: #volta o encontrou para False depois de ter verificado uma Zona
                encontrou = False


        if len(listZonas) == 0: #se estiver vazia o veiculo recebe uma das zonas para onde pode ir sem alimentos
            listPrio : list[tuple[Zona, int]] = []
            maiorPrio = 0
            for (z3, _) in listZonasSemNecessidade: # ve a maior prioridade
                if z3.getPrioridade() > maiorPrio:
                    maiorPrio = z3.getPrioridade()
            
            for (z4, distancia4) in listZonasSemNecessidade: # guarda os com maior prio numa lista
                if z4.getPrioridade() == maiorPrio:
                    listPrio.append((z4, distancia4))

            if len(listPrio) == 0:
                return (None, 0)
            if len(listPrio) == 1: # retorna se so houver 1 com maior prio
                return listPrio.pop()
            else: # se existirem mais de uma zona vai se ver a 1 que possuir menor janela
                (proximaZona, finalDis) = listPrio.pop()
                for (z5, distancia5) in listPrio:
                    x = z5.getJanela() - z5.getIteracoes()
                    comp = proximaZona.getJanela() - proximaZona.getIteracoes()
                    if(x < comp):
                        proximaZona = z5
                        finalDis = distancia5
                return (proximaZona, finalDis)
        elif len(listZonas) == 1:
            return listZonas.pop()
        else:
            maiorPrio2 = 0
            for (z6, _) in listZonas: # ve a maior prioridade
                if z6.getPrioridade() > maiorPrio2:
                    maiorPrio = z6.getPrioridade()
            
            for (z7, distancia7) in listZonas: # guarda os com maior prio numa lista
                if z7.getPrioridade() < maiorPrio2:
                    listZonas.remove((z7, distancia7))
            if len(listZonas) == 0:
                return (None, 0)
            if len(listZonas) == 1: # retorna se so houver 1 com maior prio
                return listZonas.pop()
            else: # se existirem mais de uma zona vai se ver a 1 que possuir menor janela
                (proximaZona, finalDis) = listZonas.pop()
                for (z8, distancia8) in listZonas:
                    x = z8.getJanela() - z8.getIteracoes()
                    comp = proximaZona.getJanela() - proximaZona.getIteracoes()
                    if(x < comp):
                        proximaZona = z8
                        finalDis = distancia8
                return (proximaZona, finalDis)
            

    def takeZona(self, zona : Zona,  options : list[tuple[Zona, int]]):
        options = [opt for opt in options if opt[0] != zona] #refaz a lista em que nenhuma Zona seja a mesma que a zona dada


    def addZona (self, zona: Zona, distancia: int, options: list[tuple[Zona, int]]):
        for (existing_zona, dist) in enumerate(options):
            if existing_zona == zona:
                options.remove((existing_zona, dist))
                break
        
        options.append((zona, distancia))

    def calculateDistancia():
        return
    ##########################################
    #   Greedy - so heuristica 
    ##########################################

    def greedy(self, start : Zona, veiculo : Veiculo, iter : int, path : list[Zona] = None, visited : set = None, visit = False):

        print(start.name)
        print("Iterações até momento: "+str(self.iter))
        self.iter += 1
        path.append(start) #ira repetir a mesma zona caso n tenha como ir para outra momentaneamente
        if visit == False: visited.add(start)

        if path is None:
            path = ([currentZona], 0)
        if visited is None:
            visited = set()

        # Se não houver vizinhos disponíveis, retorna falha
        # Ordena os vizinhos pela heurística
        # Escolhe o próximo nó com menor heurística
        (nextZona, distancia) = self.proximaZona(veiculo, start, visited)
        self.consomeBens(veiculo, start) # tirar do veiculo e zona os bens em comum
        start.shouldBeBlocked() # ve se depois de tirar os bens a zona esta safe


        bens : list[Bem] = veiculo.getBensAvailable()
        if len(bens) == 0 or self.iter > iter or distancia == -1:
            #custoT = self.calcula_custo(path)
            iterCopia = self.iter - 1 #comeca com 1 iteracao a mais
            self.iter = 0
            self.zonaDefiner(0)
            return (path, iterCopia)#custoT, iterCopia)

        if nextZona is not None:
            # Atualiza o caminho e o custo
            veiculo.walkedKm(distancia) #instancias usadas para mover
            self.randomZonas(self.m_zonas)
            path.append(start)
            # Chamada recursiva para o próximo nó
            return self.greedy(nextZona, veiculo, iter, path, visited, False)
        else:
            # Atualiza o caminho e o custo
            path.append(start)
            veiculo.refuel() #refil
            self.zonaDefiner(1)
            return self.greedy(start, veiculo, iter, path, visited, True)

