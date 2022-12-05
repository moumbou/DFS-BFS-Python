from dataclasses import dataclass
from collections import deque
from queue import Queue

@dataclass
class rechercheDFS:
    graph: dict
    start: int
    end: int

    def DFS(self):

        stack = deque()
        stack.append((self.start, [self.start]))

        while stack:
            (node, path) = stack.pop()
            adjacent_nodes = [n for n in self.graph[node] if n not in path]
            for adjacent_node in adjacent_nodes:
                if adjacent_node == self.end:
                    yield path + [adjacent_node]
                else:
                    stack.append((adjacent_node, path + [adjacent_node]))