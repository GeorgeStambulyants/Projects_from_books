# Topological sort
#
# Time:


class Graph:
    '''
        oriented acyclic graph
        degree of vertex - the number of edges entering the vertex
    '''

    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.graph = {
            vertex: [] for vertex in range(1, self.number_of_vertices + 1)
        }
        self.vertex_degrees = {
            vertex: 0 for vertex in range(1, self.number_of_vertices + 1)
        }

    def add_edge(self, from_, to):
        self.graph[from_].append(to)
        self.vertex_degrees[to] += 1

    def get_vertex_degree(self, vertex):
        return self.vertex_degrees[vertex]

    def __repr__(self):
        return '{}'.format(self.graph)

    def topological_sort(self):
        linear_ordering = []
        in_degree = [
            self.get_vertex_degree(vert)
            for vert in range(1, self.number_of_vertices + 1)
        ]
        next_ = [
            vertex + 1 for vertex in range(self.number_of_vertices)
            if in_degree[vertex] == 0
        ]

        while next_:
            u = next_.pop()
            linear_ordering.append(u)
            for vert in self.graph[u]:
                if not vert:
                    break
                in_degree[vert - 1] -= 1
                if in_degree[vert - 1] == 0:
                    next_.append(vert)

        return linear_ordering
