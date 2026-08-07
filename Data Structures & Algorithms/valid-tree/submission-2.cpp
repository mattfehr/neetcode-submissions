#include <vector>
#include <numeric>

class Solution {
private:
    std::vector<int> parent;
    std::vector<int> rank;

    // Find operation with Path Compression
    int findRoot(int i) {
        if (parent[i] == i) {
            return i;
        }
        // Path compression: points node directly to the root
        return parent[i] = findRoot(parent[i]); 
    }

    // Union operation with Union by Rank
    bool unionSets(int i, int j) {
        int rootI = findRoot(i);
        int rootJ = findRoot(j);

        // If they share the same root, they are already connected -> Cycle!
        if (rootI == rootJ) {
            return false; 
        }

        // Union by rank: keep the tree shallow
        if (rank[rootI] < rank[rootJ]) {
            parent[rootI] = rootJ;
        } else if (rank[rootI] > rank[rootJ]) {
            parent[rootJ] = rootI;
        } else {
            parent[rootJ] = rootI;
            rank[rootI]++;
        }
        return true;
    }

public:
    bool validTree(int n, std::vector<std::vector<int>>& edges) {
        // Enforce the mathematical condition: a tree must have exactly n - 1 edges
        if (edges.size() != n - 1) {
            return false;
        }

        // Initialize DSU structures
        parent.resize(n);
        rank.resize(n, 0);
        // Each node is initially its own parent
        std::iota(parent.begin(), parent.end(), 0); 

        // Process every edge
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            
            // If union fails, a cycle exists
            if (!unionSets(u, v)) {
                return false;
            }
        }

        return true;
    }
};
