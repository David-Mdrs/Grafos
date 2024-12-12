from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        verticesNaoAdjacentes = set()
        for i in range(1, len(self.vertices)):
            for j in range(i):
                if len(self.matriz[i][j]) == 0:
                    verticesNaoAdjacentes.add("{}-{}".format(self.vertices[j].rotulo, self.vertices[i].rotulo))
        return verticesNaoAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.vertices)):
            if len(self.matriz[i][i]) > 0:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        indiceVertice = self.indice_do_vertice(self.get_vertice(V))
        contador = 0

        for i in range(len(self.vertices)):
            if i == indiceVertice:                                      # Caso tenha laço
                contador += len(self.matriz[i][indiceVertice]) * 2      # Incremente a quantidade x 2
            else:                                                       # Caso não
                contador += len(self.matriz[i][indiceVertice])          # Incremente apenas a quantidade

        return contador

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.vertices)):
            for j in range(i, len(self.vertices)):
                print(self.matriz[i][j])
                if len(self.matriz[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V=''):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        arestasAdjacentes = []
        indiceVertice = self.indice_do_vertice(self.get_vertice(V))
        for i in range(len(self.vertices)):
            if len(self.matriz[i][indiceVertice]) > 0:
                arestasAdjacentes += list(self.matriz[i][indiceVertice].keys())
        return arestasAdjacentes

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for i in range(len(self.vertices)):
            for j in range(i, len(self.vertices)):
                if i != j and len(self.matriz[i][j]) != 1:      # Paralela ou falta
                    return False

                if i == j and len(self.matriz[i][j]) > 0:       # Laço
                    return False
        return True
