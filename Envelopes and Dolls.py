class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        r = []
        for _, h in envelopes:
            i = bisect_left(r, h)
            if i == len(r):
                r.append(h)
            else:
                r[i] = h
        return len(r)
