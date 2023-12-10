## -----------------------------------------------------------------------------------------------------
##  Arquivo     : BranchAndBound.py
##  Conteúdo    : Implementação da função que calcula a solução exata do caixeiro viajante pelo método BranchAndBound
##  Aluno       : Filipe Pirola Santos
## -----------------------------------------------------------------------------------------------------
import numpy as np
import time
import psutil
from heapq import heappush, heappop

## @brief Encontra o uso de memória em bytes    
def getMemoryUsage():
    process = psutil.Process()
    return process.memory_info().rss

class Node:
    ## @brief Cria um nó para ser utilizado no algoritmo Branch and Bound.
    def __init__(self, bound, limit_edges, cost, solution):
        self.bound = bound
        self.limit_edges = limit_edges
        self.cost = cost
        self.solution = solution
    
    ## @brief Define a comparação de nós para a heap.
    def __lt__(self, other):
        if len(self.solution) == len(other.solution):
            return self.bound < other.bound
        return len(self.solution) > len(other.solution)

## @brief Encontra as duas menores arestas em uma lista de arestas.
def findTwoMinimumEdges(edges_list):
    weights = [edges_list[j]['weight'] for j in edges_list]
    min1 = min(weights)
    weights.remove(min1)
    min2 = min(weights) if weights else np.inf
    return min1, min2

## @brief Encontra o limite inicial para o problema do Caixeiro Viajante.
def findInitialBound(A):
    initial_limit_edges = np.array([[min(findTwoMinimumEdges(A[i])) for i in range(1, A.number_of_nodes() + 1)]])
    bound = sum(initial_limit_edges.flat)
    return bound / 2, initial_limit_edges

## @brief Encontra o limite para um nó dado uma solução parcial.
def findBound(A, solution, limit_edges, bound):
    altered_edges = np.zeros(A.number_of_nodes(), dtype=int)
    new_edges = np.array(limit_edges)
    edge_weight = A[solution[-2]][solution[-1]]['weight']
    total_sum = bound * 2

    if new_edges.ndim == 1:
        new_edges = np.array([new_edges])  # Convert to 2D array if it's 1D

    for node in solution[-2:]:
        node_index = node - 1 
        if node_index < new_edges.shape[0]:
            if new_edges[node_index][0] != edge_weight:
                total_sum -= new_edges[node_index][altered_edges[node_index]]
                total_sum += edge_weight
                altered_edges[node_index] += 1

    return total_sum / 2, new_edges

## @brief Implementa o algoritmo Branch and Bound para o problema do Caixeiro Viajante.
def branchAndBound(A):
    # Registra o tempo de início e o uso de memória antes da execução
    startTime = time.time()
    startMemory = getMemoryUsage()
    
    initial_bound, initial_limit_edges = findInitialBound(A)
    root = Node(initial_bound, initial_limit_edges, 0, [1])  
    heap = []
    heappush(heap, root)
    best_cost = np.inf
    node_count = 0

    while heap:
        current_node = heappop(heap)
        node_count += 1
        level = len(current_node.solution)

        if level > A.number_of_nodes():
            if best_cost > current_node.cost:
                best_cost = current_node.cost
        else:
            if current_node.bound < best_cost:
                for k in range(1, A.number_of_nodes() + 1):
                    if k in current_node.solution:
                        continue
                    edge_weight = A[current_node.solution[-1]][k]['weight']
                    new_bound, new_edges = findBound(A, current_node.solution + [k], current_node.limit_edges, current_node.bound)
                    if new_bound < best_cost:
                        new_node = Node(new_bound, new_edges, current_node.cost + edge_weight, current_node.solution + [k])
                        heappush(heap, new_node)


    # Calcula o tempo total de execução do algoritmo
    endTime = time.time()
    finalTime = endTime - startTime  

    # Cálcula a memória utilizada pelo algoritmo
    endMemory = getMemoryUsage()
    finalMemory = endMemory - startMemory

    return best_cost, finalTime, finalMemory

## @brief General function to find the answer
def solveTSP(graph):
    answer, time, memory = branchAndBound(graph)
    print("-----------------------")
    print("Branch and Bound")
    print("Tempo de execução: ", time)
    print("Custo de memória: ", memory)
    return answer 
