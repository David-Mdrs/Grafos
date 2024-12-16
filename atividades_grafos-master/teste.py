from meu_grafo_lista_adj_nao_dir import MeuGrafo

grafo = MeuGrafo()

# Grafo completo
grafo = MeuGrafo()
grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")

grafo.adiciona_aresta('a1', 'A', 'B')
grafo.adiciona_aresta('a2', 'B', 'C')
grafo.adiciona_aresta('a3', 'C', 'D')
grafo.adiciona_aresta('a4', 'D', 'E')
grafo.adiciona_aresta('a5', 'E', 'A')

print("Imprimindo grafo: ")
print(grafo)
print(grafo.conexo())