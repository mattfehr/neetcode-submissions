class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let encoded_string: string = "";
        for (const s of strs) {
            encoded_string += String(s.length) + '#' + s;
        }
        return encoded_string;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        const decoded: string[] = [];
        let i = 0;
        while (i < str.length) {
            let num: string = "";
            while (str[i] != '#') {
                num += str[i];
                i++;
            }
            i++;
            let length: number = parseInt(num, 10); 
            const s: string = str.slice(i, i+length);
            decoded.push(s);
            i += length;
        }
        return decoded;
    }
}
