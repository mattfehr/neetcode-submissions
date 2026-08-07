#include <vector>

using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    int count;

    UnionFind(int size) {
        parent.resize(size);
        rank.assign(size, 0); 
        count = size; 
        for (int i = 0; i < size; i++) {
            parent[i] = i; 
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Added missing semicolon
        }
        return parent[x];
    }

    // Renamed from 'union' to 'unionSets' because 'union' is a keyword
    bool unionSets(int x, int y) {
        int root_x = find(x);
        int root_y = find(y);

        if (root_x == root_y) {
            return false;
        }

        if (rank[root_x] > rank[root_y]) {
            parent[root_y] = root_x;
        } else if (rank[root_x] < rank[root_y]) {
            parent[root_x] = root_y;
        } else {
            parent[root_y] = root_x;
            rank[root_x]++;
        }

        count--;
        return true;
    }
}; // Added missing semicolon here

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        // Fixed: Stack allocation instead of using 'new'
        UnionFind uf(n); 
        
        // Fixed: Normal vector element iteration to avoid syntax error
        for (const auto& edge : edges) {
            uf.unionSets(edge[0], edge[1]);
        }

        return uf.count;
    }
};
