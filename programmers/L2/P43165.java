// https://school.programmers.co.kr/learn/courses/30/lessons/43165

package git.daily_algorithm.programmers.L2;

import java.util.*;

class P43165 {
    public int solution(int[] numbers, int target) {
        // return dfs(0, 0, numbers, target);
        return bfs(numbers, target);
    }
    
    int dfs(int depth, int sum, int[] numbers, int target) {
        if (depth == numbers.length) {
            if (sum == target) {
                return 1;
            } else {
                return 0;
            }
        }
        
        return dfs(depth + 1, sum + numbers[depth], numbers, target)
            + dfs(depth + 1, sum - numbers[depth], numbers, target);
    }
    
    int bfs(int[] numbers, int target) {
        int answer = 0;
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(0);
        
        for (int num : numbers) {
            int size = q.size();
            for (int j = 0; j < size; j++) {
                int sum = q.poll();
                q.add(sum + num);
                q.add(sum - num);
            }
        }
        
        for (int sum : q) {
            if (sum == target) {
                answer++;
            }
        }
        
        return answer;
    }
}