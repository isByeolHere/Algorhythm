import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
//    static boolean[] visited;
    static int[] pick;
    static StringBuilder out = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

//        visited = new boolean[n+1];
        pick = new int[m];
        dfs(0, 1);
        System.out.print(out.toString());
        }

    static void dfs(int depth, int start) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                out.append(pick[i]).append(' ');
            }
            out.append('\n');
            return;
        }

        for (int i = start; i <= n; i++) {
//            if (visited[i]) continue;
//            visited[i] = true;
            pick[depth] = i;
            dfs(depth + 1, i + 1);
//            visited[i] = false;
        }
      }
    }