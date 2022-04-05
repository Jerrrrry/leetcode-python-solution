def backtrack(currentnode, endnode, graph, temp, visited, res):
  if currentnode == endnode:
      res.append(temp)    
      return

  neighbours = graph[currentnode]
  for neigh_node in neighbours:
      if neigh_node in visited: continue
      visited.add(neigh_node)
      backtrack(neigh_node, endnode, graph, temp*neighbours[neigh_node], visited, res)
      visited.remove(neigh_node)
    
g = {
     "A": {"B": 6, "D": 1},
     "B": {"A": 6, "D": 2, "E": 2, "C": 5},
     "D": {"A": 1, "B": 2, "E": 1},
     "E": {"B": 2, "D": 1, "C": 5},
     "C": {"B": 5, "E": 5}
}
curr1 = "A"
curr2 = "C"    
res = []
visited = set(curr1)
backtrack(curr1, curr2, g, 1, visited, res)
print(max(res))