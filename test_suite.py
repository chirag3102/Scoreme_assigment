import unittest
from graph import Graph
from constraint_manager import ConstraintManager
from coloring_solver import ColoringSolver

class TestGraphColoring(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.constraint_manager = ConstraintManager()
        self.solver = ColoringSolver(self.graph, self.constraint_manager)

    def test_coloring_with_no_constraints(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B')
        
        self.solver.color_graph()
        coloring = self.solver.get_coloring()
        
        self.assertEqual(len(set(coloring.values())), len(self.graph.vertices))

    def test_coloring_with_pre_assigned_colors(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')
        
        self.constraint_manager.assign_color('A', 1)
        self.constraint_manager.assign_color('B', 2)
        
        self.solver.color_graph()
        coloring = self.solver.get_coloring()
        
        self.assertEqual(coloring['A'], 1)
        self.assertEqual(coloring['B'], 2)
        self.assertNotIn(coloring['C'], [1, 2])

    def test_coloring_with_excluded_colors(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B')
        
        self.constraint_manager.exclude_color('A', 1)
        
        self.solver.color_graph()
        coloring = self.solver.get_coloring()
        
        self.assertNotEqual(coloring['A'], 1)

if __name__ == '__main__':
    unittest.main()
