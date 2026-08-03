class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int rows = grid.size();
        int cols = grid[0].size();
        int count = 0;
        
        vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        
        // Helper lambda function for DFS to capture variables easily
        auto dfs = [&](auto& self, int r, int c) -> void {
            // Out of bounds check or water check
            if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == '0') {
                return;
            }
            
            // Mark as visited
            grid[r][c] = '0';
            
            // Explore neighbors
            for (const auto& [dr, dc] : dirs) {
                self(self, r + dr, c + dc);
            }
        };

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == '1') {
                    dfs(dfs, r, c);
                    count++;
                }
            }
        }
        
        return count;
    }
};
