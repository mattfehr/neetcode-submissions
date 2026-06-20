class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        print(encoded_string)
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            print(i)
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            print(num, s[i])
            #s[i] = #
            i += 1
            string = ""
            for j in range(i, i+int(num)):
                string += s[j]
            print(string)
            
            decoded_string.append(string)
            i = i+int(num)
        return decoded_string

            
