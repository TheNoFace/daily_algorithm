// https://school.programmers.co.kr/learn/courses/30/lessons/43163

package git.daily_algorithm.programmers.L3;

import java.util.ArrayDeque;
import java.util.Queue;

public class P43163 {
    public int solution(String begin, String target, String[] words) {
        return bfs(begin, target, words);
    }

    int bfs(String begin, String target, String[] words) {
        Queue<Integer> q = new ArrayDeque<>();
        int[] visited = new int[words.length];
        q.add(-1);

        while (!q.isEmpty()) {
            int v = q.poll();
            if (v != -1) {
                begin = words[v];
            }

            if (begin.equals(target)) {
                for (int i = 0; i < words.length; i++) {
                    if (words[i].equals(target)) {
                        return visited[i];
                    }
                }
            }

            for (int i = 0; i < words.length; i++) {
                int count = 0;

                for (int j = 0; j < begin.length(); j++) {
                    if (visited[i] == 0 && begin.charAt(j) != words[i].charAt(j)) {
                        count++;
                    }
                }

                if (count == 1) {
                    visited[i] = v == -1 ? visited[0] + 1 : visited[v] + 1;
                    q.add(i);
                }
            }
        }
        return 0;
    }
}
