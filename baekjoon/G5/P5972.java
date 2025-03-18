import java.io.*;
import java.util.*;

public class P5972 {

    static class Node {
        int cost;
        int node;

        public Node(int node, int cost) {
            this.cost = cost;
            this.node = node;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<List<Node>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            // 비용과 다음 노드
            Node node_a = new Node(a - 1, c);
            Node node_b = new Node(b - 1, c);

            adjList.get(a - 1).add(node_b);
            adjList.get(b - 1).add(node_a);
        }

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);

        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.cost - b.cost);

        pq.offer(new Node(0, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int accumCost = current.cost;
            int currentNode = current.node;

            if (distance[currentNode] >= accumCost) {
                for (Node node : adjList.get(currentNode)) {
                    int nextCost = node.cost;
                    int nextNode = node.node;

                    int costSum = accumCost + nextCost;
                    if (distance[nextNode] > costSum) {
                        distance[nextNode] = costSum;
                        pq.add(new Node(nextNode, costSum));
                    }
                }
            }
        }

        System.out.println(distance[n - 1]);
    }
}
