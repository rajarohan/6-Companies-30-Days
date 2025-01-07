class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        r, se = set(), set()
        for i in range(len(s) - 9):
            if s[i:i + 10] in se:
                r.add(s[i:i + 10])
            se.add(s[i:i + 10])
        return list(r)
