class Solution {
    static boolean[] visited;
    static int n;
    
    public int solution(int n, int[][] computers) {
        this.n = n;
        visited = new boolean[n];
        
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]){
                dfs(i, computers);
                answer++; 
            }
        }
        
        return answer;
    }
    
    static void dfs(int node, int[][] computers){
        visited[node] = true;
        
        for (int next = 0; next < n; next++) {
            if (computers[node][next] == 1 && !visited[next]) {
                dfs(next, computers);
            }
        }
    }
}