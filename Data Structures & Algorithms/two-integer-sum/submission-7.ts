class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const diffs = new Map<number, number>();

        for (let i = 0; i < nums.length; i++) {
            const diff: number = target - nums[i];

            // If the difference exists in our map, we found our pair!
            if (diffs.has(diff)) {
                return [diffs.get(diff)!, i];
            }

            // Otherwise, store the current number and its index
            diffs.set(nums[i], i);
        }
    }
}
