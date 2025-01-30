from meu_grafo_lista_adj_nao_dir import MeuGrafo

# Grafo completo
g_6 = MeuGrafo()
g_6.adiciona_vertice("A")
g_6.adiciona_vertice("B")
g_6.adiciona_vertice("C")
g_6.adiciona_vertice("D")
g_6.adiciona_vertice("E")
g_6.adiciona_vertice("F")
g_6.adiciona_vertice("G")
g_6.adiciona_aresta("a1", "A", "B",1)
g_6.adiciona_aresta("a2", "A", "C",4)
g_6.adiciona_aresta("a3", "B", "D",5)
g_6.adiciona_aresta("a4", "D", "E",2)
g_6.adiciona_aresta("a5", "E", "G",2)
g_6.adiciona_aresta("a6", "C", "F",3)
g_6.adiciona_aresta("a7", "F", "G",4)
g_6.adiciona_aresta("a8", "C", "D",1)
g_6.adiciona_aresta("a9", "D", "F",1)

print("Imprimindo grafo: ")
print(g_6)

print(g_6.dijkstra('A', 'E'))