class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int res = 0;
        for(int i = 0; i < nums.size(); i++){
            int currgcd = nums[i];
            for(int j = i; j < nums.size(); j++){
                currgcd = gcd(currgcd,nums[j]);
                if(currgcd == k){
                    res++;
                }
            }
        }
        return res;
    }
};
