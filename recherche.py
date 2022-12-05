from graph import Graph
from dfs import rechercheDFS
from bfs import rechercheBFS
from Aetoile import A
from dataclasses import dataclass

@dataclass
class Recherche:
    methode: int
    graph: list
    start: int
    end: int

    def search(self):
        g = Graph(self.graph, [], {}).convertToGraph()
        result = None
        if self.methode == 0:
            result = rechercheDFS(g, self.start, self.end).DFS()
            result = next(result)
        if self.methode == 1:
            result = rechercheBFS(g, self.start, self.end).BFS()
            minimumParcour = []
            minimum = None
            for r in result:
                if not minimum:
                    minimum = len(r)
                
                if minimum >= len(r):
                    minimumParcour = r

            result = minimumParcour


        if self.methode == 2:
            result = A(g, self.start, self.end).search()

        graphToDraw = Graph.convertToTuple(result)
        Graph.draw(graphToDraw)