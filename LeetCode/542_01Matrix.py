class Solution:
    def bfs(self, queue, mat, dist):
        while len(queue) > 0:
            r, c = queue.pop(0)
            if r > 0 and dist[r-1][c] > dist[r][c] + 1:
                dist[r-1][c] = dist[r][c] + 1
                queue.append((r-1, c))
            if r < len(mat)-1 and dist[r+1][c] > dist[r][c] + 1:
                dist[r+1][c] = dist[r][c] + 1
                queue.append((r+1, c))
            if c > 0 and dist[r][c-1] > dist[r][c] + 1:
                dist[r][c-1] = dist[r][c] + 1
                queue.append((r, c-1))
            if c < len(mat[0])-1 and dist[r][c+1] > dist[r][c] + 1:
                dist[r][c+1] = dist[r][c] + 1
                queue.append((r, c+1))
                        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[1000000]*len(mat[0]) for i in range(len(mat))]
        queue = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        self.bfs(queue, mat, dist)
        return dist