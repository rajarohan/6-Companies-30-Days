class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        o = ""
        while columnNumber > 0:
            o = chr(ord('A') + (columnNumber - 1) % 26) + o
            columnNumber = (columnNumber - 1) // 26
        return o
