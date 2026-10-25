class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        '''
            BFS - to mark the all cells
        '''
        def BFS(i,j):
            pq = deque([])
            pq.append((i,j))
            visited[i][j] = True
            while pq:
                r,c = pq.popleft()
                for dr,dc in drs:
                    nr,nc = r+dr,c+dc
                    if nr<0 or nr>=n or nc<0 or nc>=m or grid[nr][nc] == 1 or visited[nr][nc]:
                        continue
                    pq.append((nr,nc))
                    visited[nr][nc] = True
            

        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        drs = [(0,-1),(0,1),(1,0),(-1,0)]
        for c in range(m):
            if grid[0][c] == 0 and not visited[0][c]:
                BFS(0,c)
            if grid[n-1][c] == 0 and not visited[n-1][c]:
                BFS(n-1,c)
        
        for r in range(n):
            if grid[r][0] == 0 and not visited[r][0]:
                BFS(r,0)
            if grid[r][m-1] == 0 and not visited[r][m-1]:
                BFS(r,m-1)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and not visited[i][j]:
                    cnt+=1
                    BFS(i,j)
        
        return cnt