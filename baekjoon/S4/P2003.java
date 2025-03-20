// Referenced
// https://void2017.tistory.com/333

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int count = 0;
        long sum = 0;
        int s = 0, e = 0;
        while (s < N) {
            if (sum >= M) {
                sum -= arr[s++];
            } else if (e == N) {
                break;
            } else if (sum < M) {
                sum += arr[e++];
            }

            if (sum == M) {
                count++;
            }
        }
        System.out.println(count);
    }
}
