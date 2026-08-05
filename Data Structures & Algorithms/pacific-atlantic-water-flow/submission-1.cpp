#include <vector>

using namespace std;

class Solution {
private:
    int rows, cols;
    
    void dfs(int r, int c, vector<vector<bool>>& reachable, int prev_height, const vector<vector<int>>& heights) {
        // 1. Boundary check
        if (r < 0 || r >= rows || c < 0 || c >= cols) return;
        
        // 2. Prevent infinite loops (already visited)
        if (reachable[r][c]) return;
        
        // 3. Water physics check: water flows uphill in reverse, 
        // so current cell must be >= previous cell
        if (heights[r][c] < prev_height) return;
        
        // Mark cell as reachable by this ocean
        reachable[r][c] = true;
        
        // 4. Traverse all 4 cardinal directions
        dfs(r + 1, c, reachable, heights[r][c], heights);
        dfs(r - 1, c, reachable, heights[r][c], heights);
        dfs(r, c + 1, reachable, heights[r][c], heights);
        dfs(r, c - 1, reachable, heights[r][c], heights);
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) return {};
        
        rows = heights.size();
        cols = heights[0].size();
        
        // 2D grids to track ocean reachability
        vector<vector<bool>> pacific(rows, vector<bool>(cols, false));
        vector<vector<bool>> atlantic(rows, vector<bool>(cols, false));
        
        // 1. Start DFS from Top (Pacific) and Bottom (Atlantic) borders
        for (int c = 0; c < cols; ++c) {
            dfs(0, c, pacific, heights[0][c], heights);
            dfs(rows - 1, c, atlantic, heights[rows - 1][c], heights);
        }
        
        // 2. Start DFS from Left (Pacific) and Right (Atlantic) borders
        for (int r = 0; r < rows; ++r) {
            dfs(r, 0, pacific, heights[r][0], heights);
            dfs(r, cols - 1, atlantic, heights[r][cols - 1], heights);
        }
        
        // 3. Find the intersection where cells can reach both oceans
        vector<vector<int>> result;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.push_back({r, c});
                }
            }
        }
        
        return result;
    }
};
