"""This file contains an implementation of a Graph and Dijkstra's
shortest path algorithm"""

from math import inf

class Edge:
    """Connects vertices in a graph"""
    def __init__(self,connection:tuple, weight:float = 0) -> None:
        self.connection = connection
        self.weight = weight

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
    
    def dijkstra_shortest_path(self, start, end) -> list[str]:
        """Returns the shortest path from one vertex to another using
        dijkstra's algorithm"""

        # Create shortest path dict
        shortest_path = {start:0}
        current_vertex = start
        
        # Set all other vertices to infinity
        for v in self.vertex_dict:
            shortest_path[v] = inf
        
        for _ in range(len(shortest_path)):
            # Get adjacent edges
            edges = self.get_edges(current_vertex)

        





        


        