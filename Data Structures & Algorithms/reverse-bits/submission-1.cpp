class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t sol = 0;
        for (int i = 0; i < 32; ++i) {
            uint32_t bit = (n >> i) & 1; //extract the ith bit of n
            sol += (bit << (31-i)); //shift bit to position 31-i
        }
        return sol;
    }
};
