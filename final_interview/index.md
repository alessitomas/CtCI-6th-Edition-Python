# 261. Graph Valid Tree

## Description

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

A valid tree must satisfy the following properties:
1. The graph must be connected (all nodes must be reachable from any other node)
2. The graph must not contain any cycles

## Reference

This problem is from [LeetCode Problem #261: Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

## Solution

### Primary Approach: Breadth-First Search (BFS)

The BFS approach is intuitive and efficient for this problem. Here's how it works:

1. **Early Validation**:
   - Check if the number of edges is exactly n-1 (a tree must have n-1 edges)
   - If not, return false immediately

2. **Graph Representation**:
   - Create an adjacency list representation of the graph
   - Each node points to its neighbors

3. **BFS Implementation**:
   - Start BFS from node 0
   - Keep track of visited nodes and parent nodes
   - Use a queue that stores (node, parent) pairs
   - For each node:
     - Skip the parent node to avoid false cycle detection
     - If we find a visited node that isn't the parent, we've found a cycle
     - Otherwise, add unvisited neighbors to the queue

4. **Final Validation**:
   - After BFS completes, check if all nodes were visited
   - If not all nodes were visited, the graph is not connected

### Time and Space Complexity

- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges
- **Space Complexity**: O(V) for the visited set and queue

### Alternative Approaches

1. **Union-Find (Disjoint Set)**:
   - Can be used to detect cycles while building the graph
   - Time Complexity: O(E * α(n)), where α(n) is the inverse Ackermann function
   - Space Complexity: O(n)

2. **Depth-First Search (DFS)**:
   - Similar to BFS but uses a stack/recursion instead of a queue
   - Same time and space complexity as BFS
   - May be less intuitive for this specific problem

The BFS approach is often preferred because:
- It's more intuitive to understand
- It's efficient for this problem
- It naturally handles the cycle detection and connectivity check in a single pass
