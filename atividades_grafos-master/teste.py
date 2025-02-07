from meu_grafo_lista_adj_nao_dir import MeuGrafo

# Grafo completo
grafo = MeuGrafo()
grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")

grafo.adiciona_aresta("a1", "A", "B", -1)
grafo.adiciona_aresta("a2", "B", "D", 1)
grafo.adiciona_aresta("a3", "A", "C", 5)
grafo.adiciona_aresta("a4", "C", "D", -4)
grafo.adiciona_aresta("a5", "C", "E", 3)
grafo.adiciona_aresta("a6", "E", "D", 2)

print("Imprimindo grafo: ")
print(grafo)

print(grafo.bellman_ford('A'))