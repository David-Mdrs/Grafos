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
                    return True, self.arestas[i]
                elif(self.arestas[i].v1.rotulo == self.arestas[j].v2.rotulo and self.arestas[i].v2.rotulo ==
                      self.arestas[j].v1.rotulo):
                    return True, self.aresta[i]
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
        for i in (self.arestas):
            if self.arestas[i].v1.rotulo == V:
                arestas.add(i)
            if self.arestas[i].v2.rotulo == V:
                arestas.add(i)
        return set(sorted(arestas))

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
        '''
        Depth-First Search - Busca em PROFUNDIDADE.
        Função retorna uma árvore de busca em PROFUNDIDADE.
        '''
        arvoreDFS = MeuGrafo()
        arvoreDFS.adiciona_vertice(V)
        return self.dfs_rec(V, arvoreDFS)

    def dfs_rec(self, V, arvoreDFS):
        '''
        Através de recursão, crie uma árvore de busca em PROFUNDIDADE.
        Utilizando função auxiliar proximo_vertice() para incrementar na árvore.
        '''
        arestas = sorted(self.arestas_sobre_vertice(V))     # Obtém as arestas conectadas ao vértice
        for aresta in arestas:                      # Interando sobre cada aresta
            v1, v2, rotulo = self.arestas[aresta].v1.rotulo, self.arestas[aresta].v2.rotulo, self.arestas[aresta].rotulo
            # Adicionando vértice e aresta caso não acessado
            if(v1 not in arvoreDFS.rotulos_vertices()):
                self.proximo_vertice(arvoreDFS, v2, v1, rotulo)
                self.dfs_rec(v1, arvoreDFS)
            if(v2 not in arvoreDFS.rotulos_vertices()):
                self.proximo_vertice(arvoreDFS, v1, v2, rotulo)
                self.dfs_rec(v2, arvoreDFS)

        return(arvoreDFS)

    def bfs(self, V=''):
        '''
        Breadth-First Search - Busca em LARGURA.
        Função retorna uma árvore de busca em LARGURA.
        '''
        arvoreBFS = MeuGrafo()
        arvoreBFS.adiciona_vertice(V)
        verticesNaoVisitados = [V]
        return self.bfs_rec(verticesNaoVisitados, arvoreBFS)

    def bfs_rec(self, verticesNaoVisitados, arvoreBFS):
        '''
        Através de recursão, crie uma árvore de busca em LARGURA.
        Utilizando função auxiliar proximo_vertice() para incrementar na árvore.
        '''
        if not verticesNaoVisitados:                        # Se não restar vértices a busca acabou
            return arvoreBFS

        V = verticesNaoVisitados.pop(0)                     # Remove o próximo vértice da fila
        arestas = sorted(self.arestas_sobre_vertice(V))     # Obtém as arestas conectadas ao vértice

        for aresta in arestas:                                      # Interando sobre cada aresta
            v1, v2 , rotulo = self.arestas[aresta].v1.rotulo, self.arestas[aresta].v2.rotulo, self.arestas[aresta].rotulo
            proximoVertice = v2 if v1 == V else v1                  # Determina o próximo vértice conectado

            if proximoVertice not in arvoreBFS.rotulos_vertices():  # Se o vértice ainda não foi visitado
                self.proximo_vertice(arvoreBFS, V, proximoVertice, rotulo)  # Adiciona o vértice à árvore
                verticesNaoVisitados.append(proximoVertice)         # Adiciona o próximo vértice à fila

        return self.bfs_rec(verticesNaoVisitados, arvoreBFS)

    def ha_ciclo(self):
        '''
        Função que retorna uma lista com um ciclo, caso exista.
        '''

        if self.ha_paralelas():  # Testando paralelas no grafo
            paralela = self.ha_paralelas()[1]
            ciclo = [paralela.v1.rotulo, paralela.rotulo, paralela.v2.rotulo]
            return ciclo

        arvore_dfs = self.dfs(self.rotulos_vertices()[0])   # Gera a árvore DFS a partir do primeiro vértice
        arestas_dfs = list(arvore_dfs.arestas.keys())       # Arestas da árvore DFS (usando lista)
        arestas_originais = list(self.arestas.keys())       # Arestas do grafo original (usando lista)

        # Verifica se há arestas no grafo original que não estão na árvore DFS
        arestas_extras = [aresta for aresta in arestas_originais if aresta not in arestas_dfs]

        if not arestas_extras:
            return False  # Não há ciclos

        # Reconstrução do ciclo a partir da primeira aresta extra detectada
        for aresta_retorno in arestas_extras:
            v1 = self.arestas[aresta_retorno].v1.rotulo
            v2 = self.arestas[aresta_retorno].v2.rotulo

            ciclo = [v1, aresta_retorno, v2]
            atual = v1

            visitados = set()                       # Conjunto para verificar vértices já visitados

            while atual != v2:
                encontrou_aresta = False
                visitados.add(atual)                # Marca o vértice como visitado

                for aresta, dados_aresta in arvore_dfs.arestas.items():
                    if dados_aresta.v2.rotulo == atual and dados_aresta.v1.rotulo not in visitados:
                        ciclo.insert(0, aresta)
                        ciclo.insert(0, dados_aresta.v1.rotulo)
                        atual = dados_aresta.v1.rotulo
                        encontrou_aresta = True
                        break

                if not encontrou_aresta:
                    return False

            return ciclo

        return False

    def caminho(self, n):
        if n < 1:
            return False

        vertices = sorted([str(v) for v in self.vertices])  # Ordena os vértices
        arestas_visitadas = list()
        caminho = list()

        for v in vertices:
            caminho.clear()  # Limpa o caminho
            arestas_visitadas.clear()  # Limpa as arestas visitadas
            caminho.append(v)  # Começa o caminho a partir do vértice v

            while len(caminho) <= n:
                if not caminho:  # Se o caminho estiver vazio, interrompe
                    break

                # Ordena as arestas conectadas ao vértice atual para garantir consistência
                arestas = self.arestas_sobre_vertice(caminho[-1])
                if not arestas:
                    break
                arestas = sorted(arestas, key=lambda a: str(a))  # Ordena as arestas

                for aresta in arestas:  # Interando sobre cada aresta
                    if aresta in arestas_visitadas:  # Se já foi visitada, pule
                        continue

                    v1 = self.arestas[aresta].v1.rotulo
                    v2 = self.arestas[aresta].v2.rotulo

                    proximo = v1 if v2 == caminho[-1] else v2
                    if proximo in caminho:
                        continue

                    caminho.append(proximo)
                    arestas_visitadas.append(aresta)

                    if len(caminho) == n+1:  # Caminho encontrado
                        return caminho

                    break
                else:
                    if len(caminho) <= n:  # Caminho insuficiente
                        caminho.pop()
        return False

    def conexo(self):
        arvoreDFS = self.dfs(self.rotulos_vertices()[0])
        for vertice in self.vertices:
            if vertice not in arvoreDFS.vertices:
                return False
        return True

    def dijkstra(self, verticeInicial, verticeFinal):
        # Caso os vértices de início e fim não estejam no grafo, retorne um erro
        if not self.existe_rotulo_vertice(verticeInicial) or not self.existe_rotulo_vertice(verticeFinal):
            raise VerticeInvalidoError

        # Inicializando dicionários para auxiliar função
        beta = {}
        gama = {}
        pi = {}

        # Inicializando os dados
        beta = { v.rotulo: float('inf') for v in self.vertices }    # Pesos de cada vértice no caminho
        gama = set()                                                # Vértices que já foram visitados
        pi = { v.rotulo: None for v in self.vertices }              # Vértices que armazena o seu antecessor

        # Inicializando contagem
        beta[verticeInicial] = 0
        verticeAtual = verticeInicial

        # Enquanto não chegar ao fim
        while verticeAtual is not None:
            gama.add(verticeAtual)                                  # Vértice visitado

            adjacentes = self.arestas_sobre_vertice(verticeAtual)   # Arestas conectadas ao vértice atual
            for aresta in adjacentes:
                arestaAtual = self.get_aresta(aresta)
                oposto = arestaAtual.v2.rotulo if arestaAtual.v1.rotulo == verticeAtual else arestaAtual.v1.rotulo

                if oposto in gama:                                  # Analisando se o vértice já foi visitado
                    continue

                novoValor = beta[verticeAtual] + arestaAtual.peso
                if novoValor < beta[oposto]:
                    beta[oposto] = novoValor
                    pi[oposto] = verticeAtual

            # Próximo vértice não visitado com o menor peso
            proximoVertice = {v.rotulo: beta[v.rotulo] for v in self.vertices if v.rotulo not in gama}
            if not proximoVertice:
                break

            # Escolhe o vértice com o menor custo
            verticeAtual = min(proximoVertice, key=proximoVertice.get)

        # Reconstrução do caminho
        caminhoFinal = []
        verticeNoCaminho = verticeFinal
        while verticeNoCaminho is not None:
            caminhoFinal.append(verticeNoCaminho)
            verticeNoCaminho = pi[verticeNoCaminho]

        caminhoFinal.reverse()
        return caminhoFinal

    def bellman_ford(self, verticeInicial, verticeFinal):
        # Caso os vértices de início e fim não estejam no grafo, retorne um erro
        if not self.existe_rotulo_vertice(verticeInicial) or not self.existe_rotulo_vertice(verticeFinal):
            raise VerticeInvalidoError

        # Inicializando dicionários para auxiliar função
        menorPeso = {}
        # visitados = {}

        # Inicializando os dados
        menorPeso = { v.rotulo: float('inf') for v in self.vertices }       # Pesos de cada vértice no caminho
        # visitados = { v.rotulo: None for v in self.vertices }             # Vértices que armazena o seu antecessor

        # Inicializando contagem
        menorPeso[verticeInicial] = 0

        # Iniciando interação sobre os vértices e seus valores
        for interacao in range (len(self.vertices) - 1):
            for vertice, valor in menorPeso.items():

                # Caso seja infinito, passe para o próximo vértice
                if valor == float('inf'):
                    continue

                # Buscando lista de arestas sobre o vertice
                arestas = self.arestas_sobre_vertice(vertice)
                for aresta in arestas:

                    # Buscando o vértice oposto
                    if self.arestas[aresta].v1.rotulo == vertice:
                        verticeOposto = self.arestas[aresta].v2.rotulo
                    else:
                        verticeOposto = self.arestas[aresta].v1.rotulo

                    if verticeOposto == verticeInicial:
                        continue

                    if valor + self.arestas[aresta].peso < menorPeso[verticeOposto]:
                        menorPeso[verticeOposto] = valor + self.arestas[aresta].peso

        print(menorPeso)

        # Enquanto não chegar ao fim
        # while verticeAtual is not None:
        #     gama.add(verticeAtual)                                  # Vértice visitado
        #
        #     adjacentes = self.arestas_sobre_vertice(verticeAtual)   # Arestas conectadas ao vértice atual
        #     for aresta in adjacentes:
        #         arestaAtual = self.get_aresta(aresta)
        #         oposto = arestaAtual.v2.rotulo if arestaAtual.v1.rotulo == verticeAtual else arestaAtual.v1.rotulo
        #
        #         if oposto in gama:                                  # Analisando se o vértice já foi visitado
        #             continue
        #
        #         novoValor = beta[verticeAtual] + arestaAtual.peso
        #         if novoValor < beta[oposto]:
        #             beta[oposto] = novoValor
        #             pi[oposto] = verticeAtual
        #
        #     # Próximo vértice não visitado com o menor peso
        #     proximoVertice = {v.rotulo: beta[v.rotulo] for v in self.vertices if v.rotulo not in gama}
        #     if not proximoVertice:
        #         break
        #
        #     # Escolhe o vértice com o menor custo
        #     verticeAtual = min(proximoVertice, key=proximoVertice.get)

        # Reconstrução do caminho
        # caminhoFinal = []
        # verticeNoCaminho = verticeFinal
        # while verticeNoCaminho is not None:
        #     caminhoFinal.append(verticeNoCaminho)
        #     verticeNoCaminho = pi[verticeNoCaminho]
        #
        # caminhoFinal.reverse()
        # return caminhoFinal


    # Métodos extras para auxílio na manipulação de outros métodos

    def rotulos_vertices(self):
        '''
        Função auxiliar que gera uma lista com os vertices do grafo.
        '''
        return [vertice.rotulo for vertice in self.vertices]

    def proximo_vertice(self, grafo, anterior, proximo, rotulo):
        '''
        Função auxiliar que incrementa em determinado grafo
        um novo vértice a partir de outro, assim como sua aresta correspondente.
        Utilizada na função dfs_rec.
        '''
        grafo.adiciona_vertice(proximo)
        grafo.adiciona_aresta(rotulo, anterior, proximo)