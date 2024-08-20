from graph import Graph
from constraint_manager import ConstraintManager
from coloring_solver import ColoringSolver

def main():
    graph = Graph()
    constraint_manager = ConstraintManager()
    solver = ColoringSolver(graph, constraint_manager)

    # Example Graph Setup
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    
    constraint_manager.assign_color('A', 1)
    constraint_manager.exclude_color('B', 1)
    
    solver.color_graph()
    
    print("Graph Coloring:")
    for vertex, color in solver.get_coloring().items():
        print(f"Vertex {vertex}: Color {color}")

if __name__ == "__main__":
    main()
