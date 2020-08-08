
'''
    Graph implementation with adjacency list. this implementation have support for both directed and undirected graph
    
    author: Ken Morel :P
'''

class Graph:

    class Vertex:
        def __init__(self, id):
            self.id = id
            self.adjacent_edges = []

    
    class Edge:
        def __init__(self, id, vertex_u_id, vertex_v_id, weight):
            self.id = None
            self.vertex_u_id = vertex_u_id
            self.vertex_v_id = vertex_v_id
            self.weight = weight
        
        def opposite_vertex_id(self, vertex_id):
            if vertex_id == self.vertex_u_id:
                return self.vertex_v_id
 
            return self.vertex_u_id
    
    
    def __init__(self, n, directed = False):
        self.vertices = [self.Vertex(i) for i in range(n)]
        self.edges = []
        self.directed = directed
        # This list is to keep track of vertices state while exploring them
        # -1: UNVISITED | 0: PROCESSING | 1: VISITED  (Its like an enum :P)
        self._vertices_state = [-1 for i in range(n)]

    def add_edge(self, vertex_u_id, vertex_v_id, weight=1):
        new_edge = self.Edge(len(self.edges), vertex_u_id, vertex_v_id, weight)
        self.edges.append(new_edge)
        self.vertices[vertex_u_id].adjacent_edges.append(new_edge)

        if not(self.directed):
            self.vertices[vertex_v_id].adjacent_edges.append(new_edge)
    
    def vertices_state(self):
        return self._vertices_state
    
    # Explore a particular vertex from the [source] to every other vertex reacheable from [source]
    def dfs(self, source):
        self._vertices_state[source] = 0
        for edge in self.vertices[source].adjacent_edges:
            vertex_v_id = edge.opposite_vertex_id(source)
            if self._vertices_state[vertex_v_id] == -1:
                self.dfs(vertex_v_id)
        self._vertices_state[source] = 1
    
    # Explore the whole graph
    def explore_with_dfs(self):
        self._vertices_state = [-1 for i in range(len(self.vertices))]
        for i in range(len(self.vertices)):
            if self.vertices[i] == -1:
               self.dfs(i)


# Test
g = Graph(5) 
# Vertices => [ Vertex[id:0],  Vertex[id:1], Vertex[id:2], Vertex[id:3], Vertex[id:4]
# Edges => []
print('Vertices \n')
for vertex in g.vertices:
    print('Vertex[id:%s] ' % vertex.id, end='\n')

g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 2)
g.add_edge(4, 2)

# Adjacency List
# 0: [ Edge[u: 0, v: 2] ]
# 1: [Edge[u: 1, v: 2]]
# 2: [ Edge[u: 0, v: 2], Edge[u: 1, v: 2], Edge[u: 3, v: 2], Edge[u: 4, v: 2] ]
# 3: [ Edge[u: 3, v: 2] ]
# 4: [ Edge[u: 4, v: 2] ]
print('\nAdjency List\n')
for vertex in g.vertices:
    print('%d: ' % vertex.id)
    for edge in vertex.adjacent_edges:
        print("Edge[u: %d, v: %d]" % (edge.vertex_u_id, edge.vertex_v_id), end=' ')
    print('\n')
''' Visually, the graph looks like this xD

           [1]
            |
            |
    [3] -- [2] -- [0]
            |
            |
           [4]
'''
# Explore the graph from vertex [4]
# Initially:
# Vertices state: [-1, -1, -1, -1, -1]
print('Vertices state (before DFS): \n')
print(g.vertices_state())
g.dfs(4)
# Vertices state (1: visited | -1: unvisited) after DFS (Depth-First-Search)
print("\nVertices state (after DFS): \n")
print(g.vertices_state())







