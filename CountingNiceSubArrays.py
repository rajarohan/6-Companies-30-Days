class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oc, r, i, c = 0, 0, 0, 0
        for e in nums:
            if e % 2 == 1:
                oc += 1
                c = 0
            while oc == k:
                if nums[i] % 2 == 1:
                    oc -= 1
                i += 1
                c += 1
            r += c
        return r
