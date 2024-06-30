"""This file contains an implementation of a Graph and Dijkstra's
shortest path algorithm"""

from math import inf

class Edge:
    """Connects vertices in a graph"""
    def __init__(self,connection:tuple, weight:float = 0) -> None:
        self.connection = connection
        self.weight = weight
    
    def other_vertex(self, vertex):
        if self.connection[0] == vertex:
            return self.connection[1]
        
        elif self.connection[1] == vertex:
            return self.connection[0]
        
        else:
            raise ValueError("Vertex not in this connection")

class Graph:
    """Implementation of a weighted, undirected graph"""
    def __init__(self, *vertex_names, edge_list = []) -> None:
        self.vertex_list = vertex_names
        self.edge_list = edge_list
    
    def add_vertex(self,vertex_name) -> None:
        """Creates a new vertex"""
        self.vertex_list.append(vertex_name)
    
    def add_edge(self,vertex_1:str ,vertex_2:str ,weight:float = 0):
        """Creates a new edge"""
        new_edge = Edge((vertex_1 ,vertex_2),
                        weight)
        self.edge_list.append(new_edge)
    
    def get_edges(self,vertex_name:str,exclude:str = None) -> list[Edge]:
        """Returns a list of edges connected to a vertex"""

        if vertex_name not in self.vertex_list:
            raise ValueError(f"No vertex named {vertex_name}")

        connected_edges = []

        for e in self.edge_list:
            # Check if the vertex is in the edge
            if vertex_name in e.connection and exclude not in e.connection:
                connected_edges.append(e)
        
        return connected_edges
    
    def dijkstra_path_distance(self, start, end) -> list[str]:
        """Returns the shortest path from one vertex to another using
        dijkstra's algorithm"""

        # Create shortest path dict and visited dict
        to_visit = []
        visited = []
        path_distance = {}
        
        # Set all other vertices to infinity
        for v in self.vertex_list:
            path_distance[v] = inf
        
        # Set starting vertex distanct to zero
        path_distance[start] = 0
        current_node = start
        
        while current_node != end:
            # Get adjacent edges
            edges = self.get_edges(current_node)

            # Loop throgh adjacent edges
            for e in edges:
                connected_to = e.other_vertex(current_node)
                new_distance = e.weight + path_distance[current_node]

                # If the new distance is smaller than the old, replace
                # distance
                if new_distance < path_distance[current_node]:
                    path_distance[connected_to] = new_distance
                
                # Add new node to connected
                to_visit.append(connected_to)
            
            visited.append(current_node)
            
            while current_node in visited:
                current_node = to_visit.pop(0)
        
        return path_distance



if __name__ == "__main__":
    graph = Graph(1,2,3,4,5,6,7,8,9,10,
                  edge_list=[
                      Edge((1,2),3),
                      Edge((2,6),15),
                      Edge((6,10),12),
                      Edge((1,3),5),
                      Edge((3,4),3),
                      Edge((4,6),1),
                      Edge((4,5),4),
                      Edge((5,6),4),
                      Edge((6,7),1),
                      Edge((7,8),5),
                      Edge((8,9),7),
                      Edge((9,10),10),
                      Edge((6,9),3),
                  ])
    
    shortest_dist = graph.dijkstra_path_distance(1,10)

    print(shortest_dist)
        





        


        