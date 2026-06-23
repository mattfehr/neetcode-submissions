class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {

        function isalnum(str: string): boolean {
            // Returns true if the string is not empty and contains ONLY letters and numbers
            return /^[a-zA-Z0-9]+$/.test(str);
        }

        let l = 0, r = s.length-1;
        while ( l < r ) {
            while (l < r && !isalnum(s[l])) l++;
            while (l < r && !isalnum(s[r])) r--;
            if (s[l].toLowerCase() != s[r].toLowerCase()) return false;
            l++;
            r--;
        }
        return true;
    }
}
