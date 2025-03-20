// Referenced
// https://velog.io/@ewoo97/BOJ-백준-30804번-과일-탕후루-JAVA

package S2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class P30804 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Map<Integer, Integer> fruits = new HashMap<>();
        int count = 0;
        int start = 0;

        for (int end = 0; end < N; end++) {
            fruits.put(arr[end], fruits.getOrDefault(arr[end], 0) + 1);

            while (fruits.size() > 2) {
                fruits.put(arr[start], fruits.get(arr[start]) - 1);

                if (fruits.get(arr[start]) == 0) {
                    fruits.remove(arr[start]);
                }
                start++;
            }
            count = Math.max(count, end - start + 1);
        }
        System.out.println(count);
    }
}
