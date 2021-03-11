# Search methods

import search

ab =search.GPSProblem('A', 'B'
                       , search.romania)
count,problem=search.ramificacion_acotacion_search(ab)
#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
print("Ha pasado por este número de nodos "+str(count)+" y por estos nodos:\n"
      +str(problem.path()))
count,problem=search.ramificacion_acotacion_heuristica_search(ab)
print("Ha pasado por este número de nodos "+str(count)+" y por estos nodos:\n"
      +str(problem.path())+"\n")

ar = search.GPSProblem('A', 'R'
                       , search.romania)
count,problem=search.ramificacion_acotacion_search(ar)
print("Ha pasado por este número de nodos "+str(count)+" y por estos nodos:\n"
      +str(problem.path()))
count,problem=search.ramificacion_acotacion_heuristica_search(ar)
print("Ha pasado por este número de nodos "+str(count)+" y por estos nodos:\n"
      +str(problem.path())+"\n")

te = search.GPSProblem('T', 'E'
                       , search.romania)
count,problem=search.ramificacion_acotacion_search(te)
print("Ha pasado por este número de nodos "+str(count)+" y por estos nodos:\n"
      +str(problem.path()))
count,problem=search.ramificacion_acotacion_heuristica_search(te)
print("Ha pasado por este número de nodos "+str(count)+" y por estos nodos:\n"
      +str(problem.path())+"\n")

# Result:
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 733
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
