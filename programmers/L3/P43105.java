package git.daily_algorithm.programmers.L3;

public class P43105 {
    public int solution(int[][] triangle) {

        // 마지막 행을 복사해서 dp 배열 생성
        int n = triangle.length;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = triangle[n - 1][i];
        }

        // 두 번째 마지막 행부터 위로 올라가면서 dp 값 갱신
        // 각 위치에서 dp[j]와 dp[j+1] 중 큰 값을 현재 값에 더함
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].length; j++) {
                dp[j] = triangle[i][j] + Math.max(dp[j], dp[j + 1]);
            }
        }

        return dp[0];
    }
}
