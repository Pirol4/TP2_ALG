import Christofides as C
import TwiceAroundTheTree as T
import tsplib95
import networkx as nx
import sys

def printSolution(solution):
    print("Solução:", solution['path'])
    print("Tempo de Execução:", solution['time'])
    print("Espaço de Execução:", solution['memory'])

def getGraph(file_path):
    # Carregar instância do TSPLIB
    problem = tsplib95.load(file_path)

    # Criar um grafo a partir da instância
    graph = nx.Graph()
    for edge in problem.get_edges():
        graph.add_edge(edge[0], edge[1], weight=problem.get_weight(*edge))

    return graph

def main():
    problem = sys.argv[1]
    graph = getGraph(problem)

    christofidesAnswer = C.Christofides(graph)
    printSolution(christofidesAnswer)

    twiceAroundTheTreeAnswer = T.TwiceAroundTheTree(graph)
    printSolution(twiceAroundTheTreeAnswer)

main()
    