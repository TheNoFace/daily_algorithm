package S3;

import java.util.*;
import java.io.*;

public class P17952 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int score = 0;
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            int[] task = new int[input.length];
            for (int j = 0; j < input.length; j++) {
                task[j] = Integer.parseInt(input[j]);
            }

            if (task[0] == 1) {
                int A = task[1], T = task[2];
                score += doTask(stack, A, T);
            } else {
                if (!stack.isEmpty()) {
                    int[] popTask = stack.pop();
                    score += doTask(stack, popTask[0], popTask[1]);
                }
            }
        }
        System.out.println(score);
    }

    static int doTask(Stack<int[]> stack, int score, int time) {
        if (time == 1) {
            return score;
        } else {
            stack.push(new int[] { score, (time - 1) });
            return 0;
        }
    }
}
