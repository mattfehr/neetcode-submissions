class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const stack: string[] = [];
        const map: Record<string, string> = {
            ')': '(',
            '}': '{',
            ']': '['
        };

        for (const char of s) {
            // If the character is a closing bracket
            if (map[char]) {
                const topElement = stack.pop();
                // If the popped element doesn't match the corresponding opening bracket
                if (topElement !== map[char]) {
                    return false;
                }
            } else {
                // If it's an opening bracket, push onto stack
                stack.push(char);
            }
        }

        // Return true if stack is empty (all brackets matched)
        return stack.length === 0;
    }
}