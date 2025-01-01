class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m ,n = len(img), len(img[0])
        r = [[0] * n for _ in range(m)]
        d = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                t, c = 0, 0
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj <n:
                        t += img[ni][nj]
                        c += 1
                r[i][j] = t // c
        return r
