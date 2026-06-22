class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
         if (nums.length === 0) return 0;

        // 1. Create a unique Set for O(1) lookups
        const numSet = new Set(nums);
        let maxStreak = 0;

        // 2. Iterate directly over the unique values
        for (const num of numSet) {
            // Check if 'num' is the absolute START of a sequence
            if (!numSet.has(num - 1)) {
                let currentNum = num;
                let currentStreak = 1;

                // Incrementally find the rest of the sequence
                while (numSet.has(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                // Update the maximum found so far
                maxStreak = Math.max(maxStreak, currentStreak);
            }
        }

        return maxStreak;
    }
}
