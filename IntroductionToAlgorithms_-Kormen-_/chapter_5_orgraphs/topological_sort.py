# Topological sort
#
# Time: O(n + m), where n is the number of vertices
# and m is the number if edges


class Graph:
    '''
        oriented acyclic graph
        in-degree of vertex - the number of edges entering the vertex
    '''

    def __init__(self, number_of_vertices):
        '''
            Indexes in the list self.vertex_in_degrees represent
            respective vertices
            and each element is in_degree
        '''
        self.number_of_vertices = number_of_vertices
        self.graph = [[] for _ in range(self.number_of_vertices)]
        self.vertex_in_degree = [0] * self.number_of_vertices

    def add_edge(self, from_, to):
        self.graph[from_].append(to)
        self.vertex_in_degree[to] += 1

    def get_vertex_degree(self, vertex):
        return self.vertex_in_degree[vertex]

    def __repr__(self):
        return '{}'.format(self.graph)

    def topological_sort(self):
        linear_ordering = []
        in_degree = self.vertex_in_degree[:]
        next_ = [
            vertex for vertex in range(self.number_of_vertices)
            if in_degree[vertex] == 0
        ]

        while next_:
            u = next_.pop()
            linear_ordering.append(u)
            for vert in self.graph[u]:
                if vert is None:
                    break
                in_degree[vert] -= 1
                if in_degree[vert] == 0:
                    next_.append(vert)

        return linear_ordering
