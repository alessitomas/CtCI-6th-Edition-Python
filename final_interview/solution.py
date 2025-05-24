# tree
# each node, except the root node has exaclty one parent

# BFS SOLUTION

from collections import deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If there are no nodes, it's a valid tree
        if n == 0:
            return True
            
        # If number of edges is not n-1, it can't be a tree
        if len(edges) != n - 1:
            return False
            
        # Create adjacency list
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        # Keep track of visited nodes
        visited = set()
        
        # BFS queue stores (node, parent) pairs
        queue = deque([(0, -1)])  # Start from node 0 with no parent
        visited.add(0)
        
        while queue:
            node, parent = queue.popleft()
            
            # Check all neighbors
            for neighbor in adj_list[node]:
                # Skip the parent node
                if neighbor == parent:
                    continue
                    
                # If we've seen this node before, we found a cycle
                if neighbor in visited:
                    return False
                    
                # Add to visited and queue
                visited.add(neighbor)
                queue.append((neighbor, node))
        
        # Check if all nodes were visited (graph is connected)
        return len(visited) == n

        

        