class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = size  # Tracks the total number of connected components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected, no merge happened

        # Union by rank
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1  # Successfully merged two components into one
        return True


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # 1. Initialize the UnionFind structure with n nodes
        uf = UnionFind(n)
        
        # 2. Iterate through every edge and union the nodes
        for u, v in edges:
            uf.union(u, v)
            
        # 3. The count variable inside uf now holds the remaining components
        return uf.count
