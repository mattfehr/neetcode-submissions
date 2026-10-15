class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        //comapre how many times a bit should be set in [1,n] to how many times it is

        int n = nums.size();
        int res = 0; //build duplicate number bit by bit

        //for each bit position 0 to 31
        for (int b = 0; b < 32; b++) {
            int x=0, y =0;
            int mask = 1 << b; //shift for the bit we are checking
            for (int num : nums) {
                if (num & mask) {
                    x++;    //count how nany nums have this bit set
                }
            }
            for (int num = 1; num < n; num++) {
                if (num & mask) {
                    y++;    //count how many numbers from 1 to n-1 should have it set
                }
            }
            if (x > y) {
                res |= mask;    //the duplicater has this bit set
            }
        }
        return res;
    }
};
