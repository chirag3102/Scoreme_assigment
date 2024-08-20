class ConstraintManager:
    def __init__(self):
        self.pre_assigned_colors = {}
        self.color_exclusions = {}

    def assign_color(self, vertex, color):
        self.pre_assigned_colors[vertex] = color

    def exclude_color(self, vertex, color):
        if vertex not in self.color_exclusions:
            self.color_exclusions[vertex] = set()
        self.color_exclusions[vertex].add(color)

    def get_pre_assigned_color(self, vertex):
        return self.pre_assigned_colors.get(vertex, None)

    def get_excluded_colors(self, vertex):
        return self.color_exclusions.get(vertex, set())
