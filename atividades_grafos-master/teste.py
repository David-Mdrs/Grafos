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

grafo.adiciona_aresta("a1", "A", "B")
grafo.adiciona_aresta("a2", "A", "C")
grafo.adiciona_aresta("a3", "B", "D")
grafo.adiciona_aresta("a4", "C", "D")

print("Imprimindo grafo: ")
print(grafo)

print("Imprimindo árvore de busca em largura: ")
print(grafo.dfs("A"))

