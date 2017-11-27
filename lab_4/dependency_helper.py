import copy


class DependencyHelper:
    def __init__(self):
        self.dependencies = {}

    def __add__(self, other):
        assert len(other) == 2, "tuple must be pair"

        new_dh = self.copy()
        new_dh.add(other[0], other[1])

        return new_dh

    def __iadd__(self, other):
        assert len(other) == 2, "tuple must be pair"

        self.add(other[0], other[1])

        return self

    def __sub__(self, other):
        assert len(other) == 2, "tuple must be pair"

        new = self.copy()
        new.remove(other[0], other[1])

        return new

    def __isub__(self, other):
        assert len(other) == 2, "tuple must be pair"

        self.remove(other[0], other[1])

        return self

    def __nonzero__(self):
        return not self.has_dependencies()

    def add(self, first, second):
        if first not in self.dependencies:
            self.dependencies[first] = []

        self.dependencies[first].append(second)

    def remove(self, first, second):
        if first in self.dependencies:
            self.dependencies[first].remove(second)

    def copy(self):
        return copy.deepcopy(self)

    def get_dependent(self, element):
        return self.dependencies.get(element)

    def has_dependencies(self):
        marks = {}
        for dep in self.dependencies.keys():
            marks[dep] = 0
        for dep in self.dependencies.keys():
            if self._dfs(dep, marks):
                return True
        return False

    def _dfs(self, dep, marks):
        marks[dep] = 1
        for dependent in self.dependencies[dep]:
            mark = marks.get(dependent, 2)
            if mark == 0:
                if self._dfs(dependent, marks):
                    return True
            elif mark == 1:
                return True
        marks[dep] = 2
        return False
