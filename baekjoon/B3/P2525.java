// https://www.acmicpc.net/problem/2525
package B3;

import java.io.*;
import java.util.*;

class P2525 {

    public static void main(String[] args) throws IOException {

        final int dayTime = 60 * 24;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int hour = Integer.parseInt(st.nextToken());
        int minute = Integer.parseInt(st.nextToken());
        int duration = Integer.parseInt(br.readLine());
        int bakeTime = hour * 60 + minute + duration;

        if (bakeTime / dayTime != 0) {
            bakeTime = bakeTime - dayTime;
        }

        int finHour = bakeTime / 60;
        int finMin = bakeTime % 60;

        System.out.printf("%d %d", finHour, finMin);
    }
}
