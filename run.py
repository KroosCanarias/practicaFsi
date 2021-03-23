# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("A -> B")
node, count = search.ramificacion_acotacion_search(ab)
print("Ramificación y acotación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)
node, count = search.ram_acot_subest_search(ab)
print("Ramificación y acotación con subestimación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)

print("\n----------------------------\n")

print("A -> R")

ab = search.GPSProblem('A', 'R'
                       , search.romania)

node, count = search.ramificacion_acotacion_search(ab)
print("Ramificación y acotación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)
node, count = search.ram_acot_subest_search(ab)
print("Ramificación y acotación con subestimación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)

print("\n----------------------------\n")

print("A -> N")

ab = search.GPSProblem('A', 'N'
                       , search.romania)

node, count = search.ramificacion_acotacion_search(ab)
print("Ramificación y acotación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)
node, count = search.ram_acot_subest_search(ab)
print("Ramificación y acotación con subestimación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)

print("\n----------------------------\n")

print("A -> C")

ab = search.GPSProblem('A', 'C'
                       , search.romania)

node, count = search.ramificacion_acotacion_search(ab)
print("Ramificación y acotación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)
node, count = search.ram_acot_subest_search(ab)
print("Ramificación y acotación con subestimación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)

print("\n----------------------------\n")

print("F -> L")

ab = search.GPSProblem('F', 'L'
                       , search.romania)

node, count = search.ramificacion_acotacion_search(ab)
print("Ramificación y acotación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)
node, count = search.ram_acot_subest_search(ab)
print("Ramificación y acotación con subestimación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)

print("\n----------------------------\n")

print("S -> V")

ab = search.GPSProblem('S', 'V'
                       , search.romania)

node, count = search.ramificacion_acotacion_search(ab)
print("Ramificación y acotación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)
node, count = search.ram_acot_subest_search(ab)
print("Ramificación y acotación con subestimación\n", "Camino: ", node.path(), " ~ Nodos visitados: ", count)
