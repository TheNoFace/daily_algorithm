// https://school.programmers.co.kr/learn/courses/30/lessons/43162

package git.daily_algorithm.programmers.L3;

import java.util.*;

public class P43162 {
    static int[][] adjm;
    static boolean[] visited;

    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[computers.length];
        adjm = computers;

        for (int i = 0; i < computers.length; i++) {
            if (!visited[i]) {
                bfs(i);
                answer++;
            }
        }

        return answer;
    }

    void bfs(int v) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(v);
        visited[v] = true;

        while (!q.isEmpty()) {
            v = q.poll();
            for (int i = 0; i < adjm[v].length; i++) {
                if (adjm[v][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    q.add(i);
                }
            }
        }
    }
}
