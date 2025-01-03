class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        for i, j in combinations(range(len(nums) + 1), 2):
            ans += all(n1 < n2 for n1, n2 in pairwise(nums[:i] + nums[j:]))
        return ans
