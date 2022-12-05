from dataclasses import dataclass
from collections import deque

@dataclass
class rechercheBFS:
    graph: dict
    start: int
    end: int

    def BFS(self):
        queue = deque()
        queue.append((self.start, [self.start]))

        while queue:
            node, path = queue.popleft()
            adjacent_nodes = [n for n in self.graph[node] if n not in path]
            for adjacent_node in adjacent_nodes:
                if adjacent_node == self.end:
                    yield path + [adjacent_node]
                else:
                    queue.append((adjacent_node, path + [adjacent_node]))