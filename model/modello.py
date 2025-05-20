import networkx as nx

from database.DAO import DAO


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


if __name__ == "__main__":
    m = Model()
    m.buildGraph(1970)