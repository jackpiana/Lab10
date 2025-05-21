import matplotlib.pyplot as plt
import networkx as nx

class GraphPlotter:
    """
    creato con chatGPT
    """
    def __init__(self, graph):
        """
        Initialize the GraphPlotter with a networkx graph.
        """
        if not isinstance(graph, nx.Graph):
            raise TypeError("Input must be a networkx Graph or DiGraph object.")
        self.graph = graph

    def plot(self, layout='spring', with_labels=True, node_color='skyblue', edge_color='gray', node_size=500, font_size=10, title=None):
        """
        Plot the graph using matplotlib.

        Parameters:
        - layout: 'spring', 'circular', 'kamada_kawai', or 'shell'
        - with_labels: Whether to show node labels
        - node_color: Color of the nodes
        - edge_color: Color of the edges
        - node_size: Size of the nodes
        - font_size: Font size for labels
        - title: Title for the plot
        """
        pos = self._get_layout(layout)
        plt.figure(figsize=(8, 6))
        nx.draw(
            self.graph,
            pos,
            with_labels=with_labels,
            node_color=node_color,
            edge_color=edge_color,
            node_size=node_size,
            font_size=font_size
        )
        if title:
            plt.title(title)
        plt.axis('off')
        plt.show()

    def _get_layout(self, layout_name):
        """
        Returns the layout dictionary for positioning nodes.
        """
        if layout_name == 'spring':
            return nx.spring_layout(self.graph)
        elif layout_name == 'circular':
            return nx.circular_layout(self.graph)
        elif layout_name == 'kamada_kawai':
            return nx.kamada_kawai_layout(self.graph)
        elif layout_name == 'shell':
            return nx.shell_layout(self.graph)
        else:
            raise ValueError(f"Unsupported layout: {layout_name}")


