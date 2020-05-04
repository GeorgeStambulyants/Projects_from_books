import dijkstras_algorithm as dij_al


class Graph(dij_al.Graph):
    def __init__(self, number_of_vertices, start):
        super().__init__(number_of_vertices, start)

    def get_all_edges(self):
        '''
            returns a list of all edges
        '''
        edges = []
        for u in range(self.number_of_vertices):
            for v in self.graph[u]:
                edges.append((u, v))
        return edges

    def bellman_ford(self):
        '''
            this algorithm works even with negative weights
        '''
        edges = self.get_all_edges()
        for i in range(1, self.number_of_vertices):
            for edge in edges:
                self.relax(*edge)


if __name__ == '__main__':
    print('TEST:')
    graph = Graph(5, 0)
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 2, 7)
    graph.add_edge(2, 0, 2)
    shortest = [0, 2, 4, 7, -2]
    pred = [None, 2, 3, 0, 1]

    graph.bellman_ford()
    if graph.shortest == shortest and graph.pred == pred:
        print('OK')
    else:
         raise AssertionError(
            f'self.shortest = {graph.shortest}, shortest = {shortest}; '
            f'self.pred = {graph.pred}, pred = {pred}'
        )
