from . import Bem

class Carga:
    def __init__(self, maxCarga: int, cargaAtual: int = 0, bens: list[Bem.Bem] = {}):
        """
            maxCarga - a capacidade máxima da carga

            cargaAtual - carga atual

            bens - dicionário para armazenar bens (chave: id, valor: objeto Bem)
        """
        self.maxCarga = maxCarga
        self.cargaAtual = cargaAtual
        self.bens: list[Bem.Bem] = bens

    def to_dict(self):
        """
        Custom method to serialize the Carga instance into a dictionary.
        """
        bens = [b.to_dict() for b in self.bens]  # Assume Bem objects have a `to_dict` method
        return {
            "maxCarga": self.maxCarga,
            "cargaAtual": self.cargaAtual,
            "bens": bens
        }
    
    def from_dict(self,dict):
        lista = []
        for a in dict["bens"]:
            lista.append(Bem.Bem().from_dict(a))
        return Carga(
            dict["maxCarga"],
            dict["cargaAtual"],
            lista
        )


    def __str__(self):
        bens_info = "\n".join(bem.__str__() for bem in self.bens)
        return f"Capacidade Máxima: {self.maxCarga}kg\nCarga Atual: {self.cargaAtual}kg\nBens:\n{bens_info}"

    def restock(self, bens: list[Bem.Bem]):
        """
        Adiciona uma lista de objetos do tipo 'Bem' à carga.
        Se o bem já existir, atualiza seu peso somando ao peso atual,
        respeitando o limite de capacidade.

        bens - Lista de objetos do tipo 'Bem' (list[Bem.Bem])
        """
        for bem in bens:
            if bem in self.bens:
                # Bem já existe, tenta atualizar o peso
                bem_existente : Bem = self.bens[bem]
                peso_novo = bem_existente.getPeso() + bem.getPeso()
                
                if self.cargaAtual - bem_existente.getPeso() + peso_novo <= self.maxCarga:
                    self.cargaAtual += bem.getPeso()  # Apenas adiciona o incremento de peso
                    bem_existente.setPeso(peso_novo)
            else:
                # Bem não existe, tenta adicionar
                if self.cargaAtual + bem.getPeso() <= self.maxCarga:
                    self.bens.append(bem)
                    self.cargaAtual += bem.getPeso()

    def distribute(self, bens: list[Bem.Bem]):
        """
        Remove uma lista de objetos do tipo 'Bem' da carga.

        bens - Lista de objetos do tipo 'Bem' a serem removidos (List[Bem])
        """
        for bem in bens:
            if bem in self.bens:
                bem_removido: Bem.Bem = self.bens[bem]
                peso_removido = bem_removido.getPeso()

                # Verifica se o peso do bem removido é igual ao peso atual
                if peso_removido >= self.cargaAtual:
                    # Remove o bem do dicionário sem afetar o peso diretamente
                    self.bens.pop(bem)
                else :
                    bem_existente : Bem.Bem = self.bens[bem]
                    bem_existente.setPeso(bem_existente.getPeso() - peso_removido)
                                        
                # Atualiza a carga atual
                self.cargaAtual -= peso_removido


    def getDistributionTime(self,bens : list[Bem.Bem]):
        total = 0
        for b in bens:
            total += b.getDistributionTime()
        return total

    def getBem(self, bem: Bem.Bem):
        """
        Retorna um objeto 'Bem', se existir.
        """
        return self.bens[bem]

    def removeBem(self, bem: Bem.Bem):
        """
        Remove um objeto 'Bem', se existir.
        """
        temp : Bem.Bem = self.bens.pop(bem)
        if temp:
            self.cargaAtual -= temp.getPeso()

    def getCargaAtual(self):
        """
        Retorna a carga atual.
        """
        return self.cargaAtual
    
    def updateCargaAtual(self, addSub : int):
        """
        Atualiza a carga atual.
        """
        self.cargaAtual += addSub

    def getMaxCarga(self):
        """
        Retorna a capacidade máxima da carga.
        """
        return self.maxCarga

    def getCargaDisponivel(self):
        """
        Retorna a capacidade de carga disponivel.
        """
        return self.cargaAtual
    
    def getBens(self):
        """
        Retorna a lista de bens armazenados na carga.
        """
        return self.bens
