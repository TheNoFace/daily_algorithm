package S3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P12847 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] days = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            days[i] = Integer.parseInt(st.nextToken());
        }

        long sum = 0;
        for (int i = 0; i < M; i++) {
            sum += days[i];
        }

        long max = sum;
        for (int i = M; i < N; i++) {
            sum += days[i];
            sum -= days[i - M];

            if (max < sum) {
                max = sum;
            }
        }

        System.out.println(max);
    }
}