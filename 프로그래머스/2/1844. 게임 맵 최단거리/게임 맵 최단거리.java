import java.util.*;

class Solution {
    
    static final int[] dr = {-1, 1, 0, 0};
    static final int[] dc = {0, 0, -1, 1};    
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        int[][] dist = new int[n][m];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        
        if (maps[0][0] == 0) return -1;
        dist[0][0] = 1;
        q.offer(new int[]{0, 0});
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            
            // 목적지 도달시 바로 반환
            if (r == n-1 && c == m-1){
                return dist[r][c];
            }
            
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                if (maps[nr][nc] == 0 || dist[nr][nc] != 0) continue;
                
                dist[nr][nc] = dist[r][c] +1;
                q.offer(new int[]{nr,nc});
            }
        }
        
        return -1;
    }
}