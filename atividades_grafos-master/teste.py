from meu_grafo_lista_adj_nao_dir import MeuGrafo

grafo = MeuGrafo()

# Grafo completo
grafo = MeuGrafo()
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("A")
grafo.adiciona_vertice("F")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("G")

grafo.adiciona_aresta('a1', 'E', 'A')
grafo.adiciona_aresta('a2', 'A', 'F')
grafo.adiciona_aresta('a3', 'F', 'A')
grafo.adiciona_aresta('a4', 'B', 'A')
grafo.adiciona_aresta('a5', 'B', 'A')
grafo.adiciona_aresta('a6', 'C', 'A')
grafo.adiciona_aresta('a7', 'A', 'D')
grafo.adiciona_aresta('a8', 'D', 'C')
grafo.adiciona_aresta('a9', 'G', 'D')

print("Imprimindo grafo: ")
print(grafo)
print(grafo.caminho(1))