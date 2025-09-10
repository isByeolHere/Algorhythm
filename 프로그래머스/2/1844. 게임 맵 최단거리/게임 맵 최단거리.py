from collections import deque

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    q = deque([(0, 0)])
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
    
    return dist[n-1][m-1]