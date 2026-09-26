class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to handle negative numbers and bounds
        mask = 0xFFFFFFFF
        
        while b & mask:
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask
            
        # If the 31st bit is 1, the number is negative in 32-bit two's complement
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
