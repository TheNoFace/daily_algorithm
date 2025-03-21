// Referenced
// https://wikidocs.net/207257

package S3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P14494_dp {
    public static void main(String[] args) throws IOException {
        final int MOD = 1_000_000_007;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long[][] dp = new long[n + 1][m + 1];
        dp[0][0] = 1;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] + dp[i - 1][j - 1]) % MOD;
            }
        }

        for (int i = 0; i < n + 1; i++) {
            System.out.println(Arrays.toString(dp[i]));
        }

        System.out.println(dp[n][m]);
    }
}