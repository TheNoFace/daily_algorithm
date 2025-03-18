package S2;

import java.io.*;
import java.util.*;

public class P11724 {
    static List<List<Integer>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;

            adjList.get(u).add(v);
            adjList.get(v).add(u);
        }

        boolean[] visited = new boolean[N];

        int count = 0;
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                bfs(i, visited);
                count++;
            }
        }

        System.out.println(count);
    }

    static void bfs(int v, boolean[] visited) {
        Deque<Integer> q = new ArrayDeque<>();
        q.addLast(v);
        visited[v] = true;

        while (!q.isEmpty()) {
            v = q.poll();
            for (int adj : adjList.get(v)) {
                if (!visited[adj]) {
                    visited[adj] = true;
                    q.add(adj);
                }
            }
        }
    }
}
