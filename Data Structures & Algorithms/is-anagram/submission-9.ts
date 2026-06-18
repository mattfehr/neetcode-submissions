class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) return false;
        let chars: number[] = new Array(26).fill(0);

        for (let i: number = 0; i < s.length; i++) {
            chars[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            chars[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }

        return chars.every(c => c === 0);
    }
}
