#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    unordered_set<int> visited, path;
    vector<vector<int>> adjList; // Correct dynamic initialization

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Initialize the adjacency list with the correct size
        adjList.resize(numCourses);
        for (auto& edge : prerequisites) {
            int course = edge[0];
            int prereq = edge[1];
            adjList[course].push_back(prereq);
        }

        // Run DFS for each course
        for (int i = 0; i < numCourses; ++i) {
            if (!dfs(i)) {
                return false;
            }
        }
        return true; // Added missing return statement
    }

    bool dfs(int node) {
        if (visited.count(node)) { // Corrected .contains() syntax for older C++ compatibility
            return true;
        }
        if (path.count(node)) {
            return false;
        }

        path.insert(node); // Added missing semicolon

        for (int n : adjList[node]) {
            if (!dfs(n)) {
                return false;
            }
        }

        path.erase(node); // Changed .remove() to .erase()
        visited.insert(node);
        return true;
    }
};
