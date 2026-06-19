class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let groups: Map<string, string[]> = new Map();
        for (const s of strs) {
            let counts: number[] = new Array(26).fill(0);

            for (const c of s) {
                counts[c.charCodeAt(0)-"a".charCodeAt(0)]++;
            }
            let key = "";
            for (let i = 0; i < 26; ++i) {
                key += String.fromCharCode("a".charCodeAt(0) + i) + counts[i];
            }
            if (!groups.has(key)) {
                groups.set(key, []);
            }
            groups.get(key)!.push(s);
        }
        return Array.from(groups.values());
    }
}
