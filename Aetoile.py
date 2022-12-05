from dataclasses import dataclass
from collections import deque
from graph import Graph

@dataclass
class A:
    graph: dict
    start: int
    end: int

    def solutions(self):
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

    def search(self):
        listOfSolutions = []
        solutions = self.solutions()
        for s in solutions:
            listOfSolutions.append(s)
        
        couts = []
        listDesCouts = []
        coutChoisi = None
        for solution in listOfSolutions:
            cout = len(Graph.convertToTuple(solution)) + self.end
            listDesCouts.append(cout)
            couts.append({cout: solution})
        
        minus = None
        for c in couts:
            value = next(iter(c.keys()))
            if not minus:
                minus = c
                coutChoisi = value

            if value < coutChoisi:
                coutChoisi = value
                minus = c

        if minus:
            print(f"les liste des couts de tout les chemins possible sont : {listDesCouts}")
            print(f"le cout du chemin choisi est de {coutChoisi}")
            return minus[coutChoisi]
        else:
            return []