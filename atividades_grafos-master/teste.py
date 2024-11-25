from meu_grafo_lista_adj_nao_dir import MeuGrafo

grafo = MeuGrafo()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("F")
grafo.adiciona_vertice("G")

grafo.adiciona_aresta("a1", "A", "B")
grafo.adiciona_aresta("a2", "A", "C")
grafo.adiciona_aresta("a3", "A", "D")
grafo.adiciona_aresta("a4", "B", "E")
grafo.adiciona_aresta("a5", "B", "F")
grafo.adiciona_aresta("a6", "C", "G")
grafo.adiciona_aresta("a7", "F", "G")

print("Imprimindo grafo: ")
print(grafo)

print("Imprimindo árvore de busca em profundidade: ")
print(grafo.dfs("A"))

