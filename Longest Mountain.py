class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = 0
        for indx in range(1, len(A) - 1):
            if A[indx - 1] < A[indx] > A[indx + 1]:
                l = r = indx
                while l > 0 and A[l] > A[l - 1]:
                    l -= 1
                while r + 1 < len(A) and A[r] > A[r + 1]:
                    r += 1
                res = max(res, (r - l + 1))
        return res
