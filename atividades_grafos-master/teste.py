from meu_grafo_matriz_adj_dir import MeuGrafo

# Grafo completo
grafo = MeuGrafo()
grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")

grafo.adiciona_aresta('a1', 'A', 'B')
grafo.adiciona_aresta('a2', 'A', 'C')
grafo.adiciona_aresta('a3', 'C', 'E')
grafo.adiciona_aresta('a4', 'E', 'A')
grafo.adiciona_aresta('a5', 'D', 'A')
grafo.adiciona_aresta('a6', 'D', 'E')

print("Imprimindo grafo: ")
print(grafo)

grafo.warshall()