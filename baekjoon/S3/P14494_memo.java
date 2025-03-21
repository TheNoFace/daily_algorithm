// Referenced
// https://wikidocs.net/207257

package S3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P14494_memo {
    static int n, m;
    static int[][] grid;
    static BigInteger[][] memo;

    static int[] dr = new int[] { 0, 1, 1 };
    static int[] dc = new int[] { 1, 0, 1 };

    static int divider = (int) Math.pow(10, 9) + 7;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][m];
        memo = new BigInteger[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], BigInteger.valueOf(-1));
        }

        System.out.println(dfs(0, 0).mod(BigInteger.valueOf(divider)));
    }

    static boolean isValid(int r, int c) {
        return 0 <= r && r < n && 0 <= c && c < m;
    }

    static BigInteger dfs(int sr, int sc) {
        if (sr == n - 1 && sc == m - 1) {
            return BigInteger.valueOf(1);
        }

        if (memo[sr][sc] != BigInteger.valueOf(-1)) {
            return memo[sr][sc];
        }

        memo[sr][sc] = BigInteger.valueOf(0);
        for (int i = 0; i < 3; i++) {
            int nr = sr + dr[i], nc = sc + dc[i];

            if (isValid(nr, nc)) {
                memo[sr][sc] = memo[sr][sc].add(dfs(nr, nc));
            }
        }
        return memo[sr][sc];
    }
}