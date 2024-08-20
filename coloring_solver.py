from constraint_manager import ConstraintManager
from heuristic_optimizer import HeuristicOptimizer

class ColoringSolver:
    def __init__(self, graph, constraint_manager):
        self.graph = graph
        self.constraint_manager = constraint_manager
        self.coloring = {}
        self.optimizer = HeuristicOptimizer(graph, constraint_manager)

    def color_graph(self):
        self.optimizer.optimize_coloring(self.coloring)

    def apply_dynamic_changes(self, changes):
        for change in changes:
            if change['type'] == 'add_vertex':
                self.graph.add_vertex(change['vertex'])
            elif change['type'] == 'remove_vertex':
                self.graph.remove_vertex(change['vertex'])
            elif change['type'] == 'add_edge':
                self.graph.add_edge(change['u'], change['v'])
            elif change['type'] == 'remove_edge':
                self.graph.remove_edge(change['u'], change['v'])
        self.color_graph()

    def get_coloring(self):
        return self.coloring
