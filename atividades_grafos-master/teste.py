from meu_grafo_lista_adj_nao_dir import MeuGrafo
from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON

# grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(5).arestas(True).build()
# k5 = GrafoBuilder().tipo(MeuGrafo()).vertices(5).arestas(True).build()
# GrafoJSON.grafo_to_json(k5, "test_json/k5.json")

grafo = MeuGrafo()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("F")
grafo.adiciona_vertice("G")
grafo.adiciona_vertice("H")
grafo.adiciona_vertice("I")
grafo.adiciona_vertice("J")

grafo.adiciona_aresta("a1", "A", "B")
grafo.adiciona_aresta("a2", "A", "C")
grafo.adiciona_aresta("a3", "B", "D")
grafo.adiciona_aresta("a4", "B", "E")
grafo.adiciona_aresta("a5", "C", "F")
grafo.adiciona_aresta("a6", "C", "G")
grafo.adiciona_aresta("a7", "D", "H")
grafo.adiciona_aresta("a8", "E", "H")
grafo.adiciona_aresta("a9", "F", "I")
grafo.adiciona_aresta("a10", "G", "I")
grafo.adiciona_aresta("a11", "H", "J")
grafo.adiciona_aresta("a12", "I", "J")

print("Imprimindo grafo: ")
print(grafo)

print("Imprimindo árvore de busca em profundidade: ")
print(grafo.dfs("A"))

print("Imprimindo árvore de busca em largura: ")
print(grafo.bfs("A"))
