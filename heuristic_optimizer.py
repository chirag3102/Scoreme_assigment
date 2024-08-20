import random

class HeuristicOptimizer:
    def __init__(self, graph, constraint_manager):
        self.graph = graph
        self.constraint_manager = constraint_manager

    def optimize_coloring(self, coloring):
        vertices = list(self.graph.vertices)
        random.shuffle(vertices)
        
        for vertex in vertices:
            available_colors = set(range(len(vertices)))
            pre_color = self.constraint_manager.get_pre_assigned_color(vertex)
            if pre_color is not None:
                coloring[vertex] = pre_color
                continue
            
            excluded_colors = self.constraint_manager.get_excluded_colors(vertex)
            available_colors -= excluded_colors
            
            neighbors = self.graph.get_neighbors(vertex)
            neighbor_colors = {coloring.get(neighbor) for neighbor in neighbors}
            available_colors -= neighbor_colors
            
            if available_colors:
                coloring[vertex] = min(available_colors)
            else:
                coloring[vertex] = max(coloring.values(), default=0) + 1
