class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const s: Set<number> = new Set(nums);
        return s.size != nums.length;
    }
}
