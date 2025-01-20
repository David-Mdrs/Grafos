import unittest
from meu_grafo_lista_adj_nao_dir import *
import gerar_grafos_teste
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = GrafoJSON.json_to_grafo('test_json/grafo_pb2.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = GrafoJSON.json_to_grafo('test_json/grafo_pb3.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = GrafoJSON.json_to_grafo('test_json/grafo_pb4.json', MeuGrafo())

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(['J', 'C', 'E', 'P']).arestas(True).build()

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(3).arestas(True).build()

        self.g_c3 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(1).build()

        # Grafos com laco
        self.g_l1 = GrafoJSON.json_to_grafo('test_json/grafo_l1.json', MeuGrafo())

        self.g_l2 = GrafoJSON.json_to_grafo('test_json/grafo_l2.json', MeuGrafo())

        self.g_l3 = GrafoJSON.json_to_grafo('test_json/grafo_l3.json', MeuGrafo())

        self.g_l4 = GrafoBuilder().tipo(MeuGrafo()).vertices([v:=Vertice('D')]) \
            .arestas([Aresta('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([Aresta('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo p\teste de remoção em casta
        self.g_r = GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas(1).build()

        """ Grafos para teste de dfs() e bfs() """
        # Grafos completos
        self.grafo_k5 = GrafoBuilder().tipo(MeuGrafo()).vertices(5).arestas(True).build()

        self.grafo_paralela = GrafoBuilder().tipo(MeuGrafo()).vertices(8).build()
        self.grafo_paralela.adiciona_aresta('a1', 'A', 'B')
        self.grafo_paralela.adiciona_aresta('a2', 'A', 'C')
        self.grafo_paralela.adiciona_aresta('a3', 'B', 'D')
        self.grafo_paralela.adiciona_aresta('a4', 'A', 'F')
        self.grafo_paralela.adiciona_aresta('a5', 'F', 'A')
        self.grafo_paralela.adiciona_aresta('a6', 'C', 'E')
        self.grafo_paralela.adiciona_aresta('a7', 'D', 'F')
        self.grafo_paralela.adiciona_aresta('a8', 'F', 'E')
        self.grafo_paralela.adiciona_aresta('a9', 'E', 'G')
        self.grafo_paralela.adiciona_aresta('a10', 'G', 'E')
        self.grafo_paralela.adiciona_aresta('a11', 'H', 'G')

        self.grafo_aciclico = GrafoBuilder().tipo(MeuGrafo()).vertices(8).build()
        self.grafo_aciclico.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aciclico.adiciona_aresta('a2', 'A', 'D')
        self.grafo_aciclico.adiciona_aresta('a3', 'B', 'E')
        self.grafo_aciclico.adiciona_aresta('a4', 'B', 'F')
        self.grafo_aciclico.adiciona_aresta('a5', 'A', 'C')
        self.grafo_aciclico.adiciona_aresta('a6', 'D', 'H')
        self.grafo_aciclico.adiciona_aresta('a7', 'C', 'G')
        self.grafo_aciclico.adiciona_aresta('a8', 'D', 'G')

        self.grafo_aleatorio = GrafoBuilder().tipo(MeuGrafo()).vertices(10).build()
        self.grafo_aleatorio.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aleatorio.adiciona_aresta('a2', 'A', 'C')
        self.grafo_aleatorio.adiciona_aresta('a3', 'B', 'D')
        self.grafo_aleatorio.adiciona_aresta('a4', 'B', 'E')
        self.grafo_aleatorio.adiciona_aresta('a5', 'C', 'F')
        self.grafo_aleatorio.adiciona_aresta('a6', 'C', 'G')
        self.grafo_aleatorio.adiciona_aresta('a7', 'D', 'H')
        self.grafo_aleatorio.adiciona_aresta('a8', 'E', 'H')
        self.grafo_aleatorio.adiciona_aresta('a9', 'F', 'I')
        self.grafo_aleatorio.adiciona_aresta('a10', 'G', 'I')
        self.grafo_aleatorio.adiciona_aresta('a11', 'H', 'J')
        self.grafo_aleatorio.adiciona_aresta('a12', 'I', 'J')

        """ Gabaritos para testes dfs() e bfs()"""
        self.grafo_k5_dfs = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('a1', b, a), Aresta('a2', a, c), Aresta('a8', c, d), Aresta('a10', d, e)]).build()

        self.grafo_k5_bfs = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('a1', b, a), Aresta('a5', b, c), Aresta('a6', b, d), Aresta('a7', b, e)]).build()

        self.grafo_paralela_dfs_e = GrafoBuilder().tipo(MeuGrafo()).vertices(['E', 'G', 'H', 'C', 'A', 'B', 'D', 'F']).build()
        self.grafo_paralela_dfs_e.adiciona_aresta('a10', 'E', 'G')
        self.grafo_paralela_dfs_e.adiciona_aresta('a11', 'G', 'H')
        self.grafo_paralela_dfs_e.adiciona_aresta('a6', 'E', 'C')
        self.grafo_paralela_dfs_e.adiciona_aresta('a2', 'C', 'A')
        self.grafo_paralela_dfs_e.adiciona_aresta('a1', 'A', 'B')
        self.grafo_paralela_dfs_e.adiciona_aresta('a3', 'B', 'D')
        self.grafo_paralela_dfs_e.adiciona_aresta('a7', 'D', 'F')

        self.grafo_paralela_bfs_e = GrafoBuilder().tipo(MeuGrafo()).vertices(['E', 'G', 'H', 'C', 'A', 'B', 'D', 'F']).build()
        self.grafo_paralela_bfs_e.adiciona_aresta('a10', 'E', 'G')
        self.grafo_paralela_bfs_e.adiciona_aresta('a6', 'E', 'C')
        self.grafo_paralela_bfs_e.adiciona_aresta('a8', 'E', 'F')
        self.grafo_paralela_bfs_e.adiciona_aresta('a11', 'G', 'H')
        self.grafo_paralela_bfs_e.adiciona_aresta('a2', 'C', 'A')
        self.grafo_paralela_bfs_e.adiciona_aresta('a7', 'F', 'D')
        self.grafo_paralela_bfs_e.adiciona_aresta('a1', 'A', 'B')

        self.grafo_aciclico_dfs_a = GrafoBuilder().tipo(MeuGrafo()).vertices(['A', 'B', 'E', 'F', 'D', 'H', 'G', 'C']).build()
        self.grafo_aciclico_dfs_a.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aciclico_dfs_a.adiciona_aresta('a3', 'B', 'E')
        self.grafo_aciclico_dfs_a.adiciona_aresta('a4', 'B', 'F')
        self.grafo_aciclico_dfs_a.adiciona_aresta('a2', 'A', 'D')
        self.grafo_aciclico_dfs_a.adiciona_aresta('a6', 'D', 'H')
        self.grafo_aciclico_dfs_a.adiciona_aresta('a8', 'D', 'G')
        self.grafo_aciclico_dfs_a.adiciona_aresta('a7', 'G', 'C')

        self.grafo_aciclico_bfs_a = GrafoBuilder().tipo(MeuGrafo()).vertices(['A', 'B', 'D', 'C', 'E', 'F', 'H', 'G']).build()
        self.grafo_aciclico_bfs_a.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aciclico_bfs_a.adiciona_aresta('a2', 'A', 'D')
        self.grafo_aciclico_bfs_a.adiciona_aresta('a5', 'A', 'C')
        self.grafo_aciclico_bfs_a.adiciona_aresta('a3', 'B', 'E')
        self.grafo_aciclico_bfs_a.adiciona_aresta('a4', 'B', 'F')
        self.grafo_aciclico_bfs_a.adiciona_aresta('a6', 'D', 'H')
        self.grafo_aciclico_bfs_a.adiciona_aresta('a8', 'D', 'G')

        self.grafo_aciclico_dfs_c = GrafoBuilder().tipo(MeuGrafo()).vertices(['C', 'A', 'B', 'E', 'F', 'D', 'H', 'G']).build()
        self.grafo_aciclico_dfs_c.adiciona_aresta('a5', 'C', 'A')
        self.grafo_aciclico_dfs_c.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aciclico_dfs_c.adiciona_aresta('a3', 'B', 'E')
        self.grafo_aciclico_dfs_c.adiciona_aresta('a4', 'B', 'F')
        self.grafo_aciclico_dfs_c.adiciona_aresta('a2', 'A', 'D')
        self.grafo_aciclico_dfs_c.adiciona_aresta('a6', 'D', 'H')
        self.grafo_aciclico_dfs_c.adiciona_aresta('a8', 'D', 'G')

        self.grafo_aciclico_bfs_c = GrafoBuilder().tipo(MeuGrafo()).vertices(['C', 'A', 'G', 'B', 'D', 'E', 'F', 'H']).build()
        self.grafo_aciclico_bfs_c.adiciona_aresta('a5', 'C', 'A')
        self.grafo_aciclico_bfs_c.adiciona_aresta('a7', 'C', 'G')
        self.grafo_aciclico_bfs_c.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aciclico_bfs_c.adiciona_aresta('a2', 'A', 'D')
        self.grafo_aciclico_bfs_c.adiciona_aresta('a3', 'B', 'E')
        self.grafo_aciclico_bfs_c.adiciona_aresta('a4', 'B', 'F')
        self.grafo_aciclico_bfs_c.adiciona_aresta('a6', 'D', 'H')

        self.grafo_aleatorio_dfs_a = GrafoBuilder().tipo(MeuGrafo()).vertices(['A', 'B', 'D', 'H', 'J', 'I', 'G', 'C', 'F', 'E']).build()
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a3', 'B', 'D')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a7', 'D', 'H')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a11', 'H', 'J')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a12', 'J', 'I')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a10', 'I', 'G')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a6', 'G', 'C')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a5', 'F', 'C')
        self.grafo_aleatorio_dfs_a.adiciona_aresta('a8', 'H', 'E')

        self.grafo_aleatorio_bfs_a = GrafoBuilder().tipo(MeuGrafo()).vertices(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']).build()
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a2', 'A', 'C')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a3', 'B', 'D')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a4', 'B', 'E')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a5', 'C', 'F')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a6', 'C', 'G')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a7', 'D', 'H')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a9', 'F', 'I')
        self.grafo_aleatorio_bfs_a.adiciona_aresta('a11', 'H', 'J')

        self.grafo_aleatorio_dfs_g = GrafoBuilder().tipo(MeuGrafo()).vertices(['A', 'B', 'D', 'H', 'J', 'I', 'G', 'C', 'F', 'E']).build()
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a10', 'G', 'I')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a12', 'I', 'J')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a11', 'J', 'H')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a7', 'H', 'D')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a3', 'D', 'B')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a1', 'B', 'A')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a2', 'A', 'C')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a5', 'C', 'F')
        self.grafo_aleatorio_dfs_g.adiciona_aresta('a4', 'B', 'E')

        self.grafo_aleatorio_bfs_g = GrafoBuilder().tipo(MeuGrafo()).vertices(['G',  'I', 'C', 'J', 'F', 'A', 'H', 'B', 'D', 'E']).build()
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a10', 'G', 'I')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a6', 'G', 'C')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a12', 'I', 'J')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a9', 'I', 'F')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a2', 'C', 'A')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a11', 'J', 'H')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a1', 'A', 'B')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a7', 'H', 'D')
        self.grafo_aleatorio_bfs_g.adiciona_aresta('a8', 'H', 'E')


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertIsNone(self.g_r.remove_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_aresta('1'))
        with self.assertRaises(VerticeInvalidoError):
            self.g_r.get_vertice('A')
        self.assertFalse(self.g_r.get_aresta('1'))
        self.assertEqual(self.g_r.arestas_sobre_vertice('B'), set())

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.grafo_k5.dfs("B"), self.grafo_k5_dfs)
        self.assertEqual(self.grafo_paralela.dfs("E"), self.grafo_paralela_dfs_e)
        self.assertEqual(self.grafo_aciclico.dfs("A"), self.grafo_aciclico_dfs_a)
        self.assertEqual(self.grafo_aciclico.dfs("C"), self.grafo_aciclico_dfs_c)
        self.assertEqual(self.grafo_aleatorio.dfs("A"), self.grafo_aleatorio_dfs_a)
        self.assertEqual(self.grafo_aleatorio.dfs("G"), self.grafo_aleatorio_dfs_g)

    def test_bfs(self):
        self.assertEqual(self.grafo_k5.bfs("B"), self.grafo_k5_bfs)
        self.assertEqual(self.grafo_paralela.bfs("E"), self.grafo_paralela_bfs_e)
        self.assertEqual(self.grafo_aciclico.bfs("A"), self.grafo_aciclico_bfs_a)
        self.assertEqual(self.grafo_aciclico.bfs("C"), self.grafo_aciclico_bfs_c)
        self.assertEqual(self.grafo_aleatorio.bfs("A"), self.grafo_aleatorio_bfs_a)
        self.assertEqual(self.grafo_aleatorio.bfs("G"), self.grafo_aleatorio_bfs_g)

    def test_caminho(self):
        self.assertEqual(self.g_d.caminho(1), ['A', 'B'])
        self.assertFalse(self.g_d2.caminho(1))
        self.assertEqual(self.g_p.caminho(2), ['C', 'T', 'M'])
        self.assertFalse(self.g_p.caminho(5))
        self.assertEqual(self.g_l1.caminho(1), ['A', 'B'])
        self.assertFalse(self.g_l1.caminho(4))

    def test_conexo(self):
        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.g_d2.conexo())
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p2.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_r.conexo())