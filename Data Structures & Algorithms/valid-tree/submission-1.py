class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree is just a fully connected graph with no cycles
        if len(edges) != n-1:
            return False

        adjList = [[] for i in range(n)]
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visited = set()

        #if a graph has exactly n-1 edges and is fully connected, it cant have a cycle
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)
        
        # Start DFS from a single node
        dfs(0)
        
        # If we reached every node from node 0, it's a valid tree
        return len(visited) == n