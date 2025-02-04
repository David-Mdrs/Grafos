from meu_grafo_lista_adj_nao_dir import MeuGrafo

# Grafo completo
grafo = MeuGrafo()
grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("I")

grafo.adiciona_aresta("a1", "I", "E", 8)
grafo.adiciona_aresta("a2", "E", "D", 1)
grafo.adiciona_aresta("a3", "D", "A", -2)
grafo.adiciona_aresta("a4", "I", "A", 10)
grafo.adiciona_aresta("a5", "A", "B", 1)
grafo.adiciona_aresta("a6", "B", "C", -1)
grafo.adiciona_aresta("a7", "C", "A", 6)
grafo.adiciona_aresta("a8", "D", "C", 4)

print("Imprimindo grafo: ")
print(grafo)

print(grafo.bellman_ford('I', 'A'))