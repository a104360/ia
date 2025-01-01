from .veiculos import Bem
from . import Clima

class Zona:
    def __init__(self, name, id=-1, bloqueado = False, gravidade=0, densidade=0, abastecimento = 100, acessibilidade = None, clima = {}, necessidades={}, iteracoes = 0):     
        """
            id - valor único de cada Zona

            name - nome da Zona

            bloquado - se e possivel ir para a zona ou não

            gravidade - gravidade do problema

            densidade - densidade populacional

            prioridade - o quão prioritária esta Zona é, sendo 1 o que menor prioridade tem

            abastecimento - combustivel que cada veiculo pode reabastecer ao esperar 1 iteração

            acessibilidade - lista [marítima, terrestre, aérea] (0 não tem ou 1 tem)

            clima - Lista de objetos Clima associados à Zona

            necessidades - dicionário de Bens que a Zona necessita

            iteracoes - número de iterações que passou desde a ultima vez que a prioridade foi 0
        """
        self.id = id
        self.name = name
        self.bloquado = bloqueado
        self.gravidade = gravidade
        self.densidade = densidade
        self.prioridade = self.calculatePrioridade(gravidade, densidade)
        if acessibilidade != None and (len(acessibilidade) == 3 and all(x in [False,True] for x in acessibilidade)): self.acessibilidade = acessibilidade
        else: self.acessibilidade = [False, False, False]
        self.abastecimento = abastecimento
        self.clima = list(necessidades) #: List[Clima] = clima 
        self.necessidades = list(necessidades) #: List[Bem] = necessidades
        self.iteracoes = iteracoes

    def __eq__(self, other):
        """Compara os objetos Zona apenas pelo nome"""
        if isinstance(other, Zona):
            return self.name == other.name
        return False
    

    def calculatePrioridade(self, gravidade : int, densidade : int):
        """Calcula a prioridade com base na gravidade e densidade."""
        return gravidade * densidade

    def __str__(self):
        return (f"Zona : {self.name}\nID : {self.id}\nBlocked : {self.bloquado}\n"+
                f"Gravidade : {self.gravidade}\nPriority : {self.prioridade}\n" + 
                f"Acessibilidade : {self.acessibilidade}\nAbastecimento : {self.abastecimento}\n" +
                f"Climate : {self.clima}\nNecessidades : {self.necessidades}\nIter : {self.iteracoes}")

    def __repr__(self):
        return f"Zona : {self.name}"

    # Métodos para 'id'
    def setId(self, id : int):
        """Define o ID da Zona."""
        self.id = id

    def getId(self):
        """Retorna o ID da Zona."""
        return self.id

    # Métodos para 'name'
    def setName(self, name : int):
        """Define o nome da Zona."""
        self.name = name

    def getName(self):
        """Retorna o nome da Zona."""
        return self.name

    # Métodos para 'bloqueado'
    def setBloqueado(self, bloqueado : bool):
        """Define o estado de bloqueio da Zona."""
        self.bloqueado = bloqueado

    def isBloqueado(self):
        """Retorna se a Zona está bloqueada."""
        return self.bloqueado
    
    def shouldBeBlocked(self):
        """Retorna se a Zona está deve ser bloquada ou não e retorna o estado final."""
        if self.isGoingToBeBlocked() == 0: 
            self.bloqueado = False
            return False
        else:
            self.bloquado = True
            return True
    
    # Métodos para 'gravidade'
    def setGravidade(self, gravidade : int):
        """Define a gravidade da Zona."""
        self.gravidade = gravidade
        self.prioridade = self.calculatePrioridade(self.gravidade, self.densidade)

    def getGravidade(self):
        """Retorna a gravidade da Zona."""
        return self.gravidade

    # Métodos para 'densidade'
    def setDensidade(self, densidade : int):
        """Define a densidade populacional da Zona."""
        self.densidade = densidade
        self.prioridade = self.calculatePrioridade(self.gravidade, self.densidade)

    def getDensidade(self):
        """Retorna a densidade populacional da Zona."""
        return self.densidade

    # Métodos para 'prioridade'
    def getPrioridade(self):
        """Retorna a prioridade da Zona."""
        return self.prioridade

    # Métodos para 'acessibilidade'
    def setAcessibilidadeMaritima(self, acessivel: bool):
        """Define se a Zona é acessível por via marítima."""
        self.acessibilidade[0] = acessivel

    def setAcessibilidadeTerrestre(self, acessivel: bool):
        """Define se a Zona é acessível por via terrestre."""
        self.acessibilidade[1] = acessivel

    def setAcessibilidadeAerea(self, acessivel: bool):
        """Define se a Zona é acessível por via aérea."""
        self.acessibilidade[2] = acessivel

    def setAcessibilidade(self, acessibilidade : list[bool]):
        """Define a acessibilidade da Zona."""
        if len(acessibilidade) != 3 or not all(x in [False, True] for x in acessibilidade):
            return
        self.acessibilidade = acessibilidade

    def getAcessibilidade(self):
        """Retorna a acessibilidade da Zona."""
        return self.acessibilidade

    def isAcessivelMaritima(self):
        """Retorna se a Zona é acessível por via marítima."""
        return self.acessibilidade[0]

    def isAcessivelTerrestre(self):
        """Retorna se a Zona é acessível por via terrestre."""
        return self.acessibilidade[1]

    def isAcessivelAerea(self):
        """Retorna se a Zona é acessível por via aérea."""
        return self.acessibilidade[2]

    # Métodos para 'clima'
    def isGoingToBeBlocked(self):
        """Verifica se a Zona será bloqueada com base nos climas."""
        for temp in self.clima:
            if temp.isBlocking():
                return 1
        return 0

    def addClima(self, clima : Clima):
        """Adiciona ou substitui um objeto Clima à Zona."""
        self.clima[clima] = clima

    def removeClima(self, clima : Clima):
        """Remove um objeto Clima da Zona."""
        if clima in self.clima:
            self.clima.pop(clima)

    # Métodos para 'necessidades'
    def setNecessidades(self, necessidades: list[Bem.Bem]):
        """
        Adiciona uma lista de objetos do tipo 'Bem' às necessidades.
        Se o bem já existir, atualiza seu peso somando ao peso atual.

        necessidades - Lista de objetos do tipo 'Bem' (List[Bem])
        """
        for necessidade in necessidades:
            if necessidade in self.necessidades:
                # Atualiza o peso da necessidade existente
                necessidade_existente : Bem = self.necessidades[necessidade]
                peso_novo = necessidade_existente.getPeso() + necessidade.getPeso()
                necessidade_existente.setPeso(peso_novo)
            else:
                # Adiciona um novo bem às necessidades
                self.necessidades.append(necessidade)

    def removeNecessidades(self, necessidades: list[Bem.Bem]):
        """
        Remove uma lista de objetos do tipo 'Bem' das necessidades.
        O bem será removido somente se o peso do bem for igual ao peso registrado.
        Se for removido, atualiza o peso da carga atual usando o método setPeso.

        necessidades - Lista de objetos do tipo 'Bem' (List[Bem])
        """
        for necessidade in necessidades:
            if necessidade in self.necessidades:
                necessidade_removido: Bem = self.necessidades[necessidade]
                peso_removido = necessidade_removido.getPeso()

                # Verifica se o peso do bem removido é igual ao peso atual
                if peso_removido >= self.cargaAtual:
                    # Remove o bem do dicionário sem afetar o peso diretamente
                    self.necessidades.pop(necessidade)
                    
                else :
                    necessidade_existente : Bem = self.necessidades[necessidade]
                    necessidade_existente.setPeso(necessidade_existente.getPeso() - peso_removido)

    def getNecessidades(self):
        """
        Retorna as necessidades da Zona.
        """
        return self.necessidades

    def addNecessidade(self, necessidade: Bem):
        """
        Adiciona um Bem às necessidades da Zona.

        necessidade - Objeto do tipo 'Bem'
        """
        if necessidade in self.necessidades:
            # Atualiza o peso se o Bem já existir
            necessidade_existente : Bem = self.necessidades[necessidade]
            peso_novo = necessidade_existente.getPeso() + necessidade.getPeso()
            necessidade_existente.setPeso(peso_novo)
        else:
            # Adiciona um novo Bem às necessidades
            self.necessidades.append(necessidade)

    def removeNecessidade(self, necessidade: Bem):
        """
        Remove um Bem das necessidades da Zona pelo ID.

        necessidade - Objeto do tipo 'Bem'
        """
        if necessidade in self.necessidades:
            necessidade_removido: Bem = self.necessidades[necessidade]
            peso_removido = necessidade_removido.getPeso()

            # Verifica se o peso do bem removido é igual ao peso atual
            if peso_removido >= self.cargaAtual:
                # Remove o bem do dicionário sem afetar o peso diretamente
                self.necessidades.pop(necessidade)
                    
            else :
                necessidade_existente : Bem = self.necessidades[necessidade]
                necessidade_existente.setPeso(necessidade_existente.getPeso() - peso_removido)

    #Metodos para iteracoes
    def setIteracoes(self, iteracoes : int):
        """Define a iteracao da Zona."""
        self.iteracoes = iteracoes

    def getIteracoes(self):
        """Retorna a iteracao da Zona."""
        return self.iteracoes