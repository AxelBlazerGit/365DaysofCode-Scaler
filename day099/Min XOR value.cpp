int Solution::findMinXor(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    int min_xor = nums[0] ^ nums[1];
    for (size_t i = 1; i < nums.size() - 1; ++i) {
        // int xor_val = nums[i] ^ nums[i + 1];
        min_xor = min(min_xor, nums[i] ^ nums[i + 1]);
    }
    return min_xor;
}
