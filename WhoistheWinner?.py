class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = []
        for i in range(1, n + 1):
            q.append(i)
        while len(q) > 1:
            for i in range(k - 1):
                num = q.pop(0)
                q.append(num)
            q.pop(0)
        return q[0]
