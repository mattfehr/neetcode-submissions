class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i): #check if bit at position i is 1 or 0
                binary += "1"
            else:
                binary += "0"
        
        sol = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                sol |= (1 << i) #if the bit is 1 set the corresponding bit in solution
        
        return sol
