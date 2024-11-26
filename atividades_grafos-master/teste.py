from meu_grafo_lista_adj_nao_dir import MeuGrafo
from grafo_lista_adj_test_nao_dir import TestGrafo

# from bibgrafo.grafo_builder import GrafoBuilder
# from bibgrafo.grafo_json import GrafoJSON

# grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(5).arestas(True).build()
# k5 = GrafoBuilder().tipo(MeuGrafo()).vertices(5).arestas(True).build()
# GrafoJSON.grafo_to_json(k5, "test_json/k5.json")

grafo = MeuGrafo()

# Grafo completo
g_c = MeuGrafo()
g_c.adiciona_vertice("J")
g_c.adiciona_vertice("C")
g_c.adiciona_vertice("E")
g_c.adiciona_vertice("P")
g_c.adiciona_aresta('a1', 'J', 'C')
g_c.adiciona_aresta('a2', 'J', 'E')
g_c.adiciona_aresta('a3', 'J', 'P')
g_c.adiciona_aresta('a4', 'E', 'C')
g_c.adiciona_aresta('a5', 'P', 'C')
g_c.adiciona_aresta('a6', 'P', 'E')

print("Imprimindo grafo: ")
print(g_c)

print("Imprimindo árvore de busca em profundidade: ")
print(g_c.dfs("C"))

print("Imprimindo árvore de busca em largura: ")
print(g_c.bfs("C"))
