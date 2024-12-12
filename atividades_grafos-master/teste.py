from meu_grafo_matriz_adj_nao_dir import MeuGrafo

grafo = MeuGrafo()

# Grafo completo
grafo = MeuGrafo()
grafo.adiciona_vertice("J")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("P")
grafo.adiciona_vertice("M")
grafo.adiciona_vertice("T")
grafo.adiciona_vertice("Z")

grafo.adiciona_aresta('a1', 'J', 'C')
grafo.adiciona_aresta('a2', 'C', 'E')
grafo.adiciona_aresta('a3', 'C', 'E')
grafo.adiciona_aresta('a4', 'P', 'C')
grafo.adiciona_aresta('a5', 'P', 'C')
grafo.adiciona_aresta('a6', 'T', 'C')
grafo.adiciona_aresta('a7', 'M', 'C')
grafo.adiciona_aresta('a8', 'M', 'T')
grafo.adiciona_aresta('a9', 'T', 'Z')

print("Imprimindo grafo: ")
print(grafo)
print(grafo.vertices_nao_adjacentes())