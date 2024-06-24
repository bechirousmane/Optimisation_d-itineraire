import networkx as nx
import matplotlib.pyplot as plt
from optimizationInterface import optimizationInterface

class acpm_tsp(optimizationInterface) :

    def optimizationAlgo(self, breakPoints, start) : 
       
        graph = nx.DiGraph() 

        for (i,j) , dist in breakPoints.items() :
            graph.add_edge(i, j, weight=dist)

    
        acpm = nx.minimum_spanning_tree(graph.to_undirected(), algorithm='prim')
        itinariry = self.exploresInDepth (acpm, start)

        build = acpm
        pos = nx.spring_layout(build)
        nx.draw(build, pos, with_labels = True , node_color='lightblue', node_size=700, font_size=12, font_weight='bold')
        labels = nx.get_edge_attributes(build, 'weight')       
        nx.draw_networkx_edge_labels(build , pos, edge_labels=labels)
        plt.show()

        return itinariry
    

    def exploresInDepth(self, graph,start) :

        visited = []
        toVisit = []
        visited.append(start)
            
        for neighbor in graph.neighbors(start) :
            toVisit.append(neighbor)

        while toVisit :
            node = toVisit.pop()
            visited.append(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    toVisit.append(neighbor)

        visited.append(start)
        return visited


if __name__ == "__main__" :
    breakPointss = {
    (0, 1): 2.2, (0, 2): 45, (0, 3): 3.0, (1,0) : 3.2, (2,0) : 14,
    (1, 2): 2.2, (1, 3): 1.5, (2,1) : 13, (3,2) : 5, (3,1) : 0.8,
    (2, 3): 3.6, (0,4) : 2.3, (1,4) : 12, (3,4) : 1.5, (4,3) : 2, (4,1) : 10, (4,0) : 4, (4,2) : 7
}
    start_node = 0
    acpm_tsp_solver = acpm_tsp()
    itinerary = acpm_tsp_solver.itinerary(breakPointss, start_node)
    print("Itinéraire approximatif du TSP :", itinerary)
