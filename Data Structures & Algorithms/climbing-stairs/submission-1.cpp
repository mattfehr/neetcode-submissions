#include <vector>

class Solution {
public:
    int climbStairs(int n) {
        // Initialize memoization array with -1 to represent unvisited states
        // Size is n + 1 to easily map indices from 0 to n
        std::vector<int> memo(n + 1, -1);
        return solve(0, n, memo);
    }

private:
    int solve(int current_step, int target_step, std::vector<int>& memo) {
        // Base Case 1: Successfully reached the top step
        if (current_step == target_step) {
            return 1;
        }
        // Base Case 2: Overshot the top step (invalid path)
        if (current_step > target_step) {
            return 0;
        }
        
        // Cache Hit: Return the answer if we already computed it
        if (memo[current_step] != -1) {
            return memo[current_step];
        }
        
        // Recursive Step: Sum the choices of taking 1 step or 2 steps
        int take_1_step = solve(current_step + 1, target_step, memo);
        int take_2_steps = solve(current_step + 2, target_step, memo);
        
        // Cache Miss: Store the result in memo array before returning
        memo[current_step] = take_1_step + take_2_steps;
        
        return memo[current_step];
    }
};
