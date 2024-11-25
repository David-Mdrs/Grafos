from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        verticesNA = set()
        for i in self.vertices:
            for j in self.vertices:
                if i != j and (f"{j}-{i}" not in verticesNA and f"{i}-{j}" not in verticesNA):
                    arestaAdjacente = any(
                        (self.arestas[a].v1.rotulo == str(i) and self.arestas[a].v2.rotulo == str(j)) or
                        (self.arestas[a].v1.rotulo == str(j) and self.arestas[a].v2.rotulo == str(i))
                        for a in self.arestas)
                    if not arestaAdjacente:
                        verticesNA.add(f"{i}-{j}")
        return verticesNA

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.arestas:
            if self.arestas[i].v1 == self.arestas[i].v2:
                return True
        return False

    def grau(self, V = ''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        contador = 0
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Vertice não existe no grafo!")
        for i in self.arestas:
            if self.arestas[i].v1.rotulo == V:
                contador += 1
            if self.arestas[i].v2.rotulo == V:
                contador += 1
        return contador

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in self.arestas:
            for j in self.arestas:
                if(i == j):
                    continue
                if(self.arestas[i].v1.rotulo == self.arestas[j].v1.rotulo and self.arestas[i].v2.rotulo ==
                        self.arestas[j].v2.rotulo):
                    return True
                elif(self.arestas[i].v1.rotulo == self.arestas[j].v2.rotulo and self.arestas[i].v2.rotulo ==
                      self.arestas[j].v1.rotulo):
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas = set()
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Vértice inexistente!")
        for i in self.arestas:
            if self.arestas[i].v1.rotulo == V:
                arestas.add(i)
            if self.arestas[i].v2.rotulo == V:
                arestas.add(i)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if(not(self.ha_paralelas() and self.ha_laco())): # Se não houver laços ou paralelas
            qntVertices = len(self.vertices)
            for i in self.vertices:
                if(self.grau(i.rotulo) == qntVertices-1):
                    continue
                else:
                    return False
            return True
        return False

    def dfs(self, V = ''):
        arvoreDFS = MeuGrafo()
        arvoreDFS.adiciona_vertice(V)
        return self.dfs_rec(V, arvoreDFS)

    def rotulos_vertices(self):
        return [vertice.rotulo for vertice in self.vertices]

    def dfs_rec(self, V, arvoreDFS):
        arestas = self.arestas_sobre_vertice(V)     # Inserindo novas arestas
        for aresta in arestas:                      # Interando sobre cada aresta

            if(self.arestas[aresta].v1.rotulo not in arvoreDFS.rotulos_vertices()):
                arvoreDFS.adiciona_vertice(self.arestas[aresta].v1.rotulo)
                arvoreDFS.adiciona_aresta(self.arestas[aresta].v1.rotulo + self.arestas[aresta].v2.rotulo,
                                          self.arestas[aresta].v1.rotulo, self.arestas[aresta].v2.rotulo)
                self.dfs_rec(self.arestas[aresta].v1.rotulo, arvoreDFS)

            if(self.arestas[aresta].v2.rotulo not in arvoreDFS.rotulos_vertices()):
                arvoreDFS.adiciona_vertice(self.arestas[aresta].v2.rotulo)
                arvoreDFS.adiciona_aresta(self.arestas[aresta].v1.rotulo + self.arestas[aresta].v2.rotulo,
                                          self.arestas[aresta].v1.rotulo, self.arestas[aresta].v2.rotulo)
                self.dfs_rec(self.arestas[aresta].v2.rotulo, arvoreDFS)

        return(arvoreDFS)

    def bfs(self, raiz = ''):
        # Depth-First Search - Função para busca em profundidade.
        pass