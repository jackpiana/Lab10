import networkx as nx

from database.DAO import DAO
from model.plotter import GraphPlotter


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._countries = DAO.get_all_countries()

    def buildGraph(self, anno):
        """
        creo un grafo con tutti i confini precedenti all'anno in input

        """
        if self._grafo is not None:
            self._grafo = nx.Graph()

        edges = DAO.get_edges_filtered(anno)
        for edge in edges:
            a = self._countries[edge["state1no"]]
            b = self._countries[edge["state2no"]]
            self._grafo.add_node(a)
            self._grafo.add_node(b)
            self._grafo.add_edge(a, b)
            #print(f"added edge {a} --- {b}")

    def get_componenti_connesse(self):
        return nx.number_connected_components(self._grafo)

    def get_reachable_nodes(self, node):
        reachable_nodes = nx.node_connected_component(self._grafo, node)
        return reachable_nodes

if __name__ == "__main__":
    m = Model()
    m.buildGraph(2000)
    plotter = GraphPlotter(m._grafo)
    plotter.plot(layout='spring', title='My Graph')
