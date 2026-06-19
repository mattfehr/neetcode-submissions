class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const counts = new Map<number, number>();
        for (const n of nums) {
            counts.set(n, (counts.get(n) || 0) + 1);
        } 
        return Array.from(counts.entries())
            .sort((a,b) => b[1] - a[1])
            .slice(0,k)
            .map(entry => entry[0]);
    }
}
