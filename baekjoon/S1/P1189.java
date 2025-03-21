package S1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1189 {
    static int R, C, K;
    static char[][] grid;
    static int answer = 0;
    static boolean[][] visited;

    // 상 하 좌 우
    static int[] dr = new int[] { -1, 1, 0, 0 };
    static int[] dc = new int[] { 0, 0, -1, 1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        grid = new char[R][C];

        for (int i = 0; i < R; i++) {
            char[] col = br.readLine().toCharArray();
            for (int j = 0; j < C; j++) {
                grid[i] = col;
            }
        }

        visited = new boolean[R][C];
        dfs(R - 1, 0, 1);
        System.out.println(answer);
    }

    static boolean isValid(int r, int c) {
        return 0 <= r && r < R && 0 <= c && c < C;
    }

    static void dfs(int sr, int sc, int k) {
        visited[sr][sc] = true;

        if (sr == 0 && sc == C - 1 && k == K) {
            answer++;
            return;
        }

        if (k >= K) {
            return;
        }

        for (int d = 0; d < 4; d++) {
            int nr = sr + dr[d], nc = sc + dc[d];
            if (isValid(nr, nc) && grid[nr][nc] != 'T' && !visited[nr][nc]) {
                dfs(nr, nc, k + 1);
                visited[nr][nc] = false;
            }
        }
    }
}