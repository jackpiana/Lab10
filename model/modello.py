import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._countries = DAO.get_all_countries()

    def buildGraph(self, anno):
        edges = DAO.get_edges_filtered(anno)
        for edge in edges:
            a = self._countries(edge["state1ab"])
            b = self._countries(edge["state2ab"])
            self._grafo.add_node(a)
            self._grafo.add_node(b)
            self._grafo.add_edge(a, b)
            print(f"added edge {a} --- {b}")

