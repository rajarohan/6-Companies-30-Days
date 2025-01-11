class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res, buckets = 0, dict()
        def getKey(val):
            return val // d
        def addVal(val):
            key = getKey(val)
            if key in buckets:
                if buckets[key][0] > val: buckets[key][0] = val
                elif buckets[key][1] < val: buckets[key][1] = val
            else:
                buckets[key] = [val, val]
        for val in arr2: addVal(val)
        for val in arr1:
            key = getKey(val)
            if key in buckets: continue
            if key - 1 in buckets and val - buckets[key-1][1] <= d: continue
            if key + 1 in buckets and buckets[key+1][0] - val <= d: continue
            res += 1
        return res
