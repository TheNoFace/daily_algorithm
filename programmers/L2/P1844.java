// https://school.programmers.co.kr/learn/courses/30/lessons/1844

package git.daily_algorithm.programmers.L2;

import java.util.ArrayDeque;

public class P1844 {
    static int[] dr = new int[] { -1, 1, 0, 0 };
    static int[] dc = new int[] { 0, 0, -1, 1 };

    static int n;
    static int m;

    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;

        return bfs(maps);
    }

    int bfs(int[][] maps) {

        ArrayDeque<int[]> q = new ArrayDeque<>();
        int[][] visited = new int[n][m];
        q.add(new int[] { 0, 0 });
        visited[0][0] = 1;

        while (!q.isEmpty()) {
            int[] cord = q.poll();
            int sr = cord[0], sc = cord[1];

            if (sr == n - 1 && sc == m - 1) {
                return visited[n - 1][m - 1];
            }

            for (int i = 0; i < 4; i++) {
                int nr = sr + dr[i], nc = sc + dc[i];
                if (isValid(nr, nc) && maps[nr][nc] != 0 && visited[nr][nc] == 0) {
                    q.add(new int[] { nr, nc });
                    visited[nr][nc] = visited[sr][sc] + 1;
                }
            }
        }
        return -1;
    }

    boolean isValid(int r, int c) {
        return (0 <= r && r < n && 0 <= c && c < m);
    }
}
