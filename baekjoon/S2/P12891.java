package S2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P12891 {
    static int[] count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        char[] dna = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());
        int[] criteria = new int[4];
        for (int i = 0; i < 4; i++) {
            criteria[i] = Integer.parseInt(st.nextToken());
        }

        int result = 0;

        count = new int[4];
        for (int i = 0; i < P; i++) {
            addToPw(dna[i]);
        }

        if (isMatch(criteria, count)) {
            result++;
        }

        for (int i = P; i < S; i++) {
            addToPw(dna[i]);
            deleteFromPw(dna[i - P]);

            if (isMatch(criteria, count)) {
                result++;
            }
        }
        System.out.println(result);
    }

    static void addToPw(char c) {
        switch (c) {
            case 'A':
                count[0]++;
                break;
            case 'C':
                count[1]++;
                break;
            case 'G':
                count[2]++;
                break;
            case 'T':
                count[3]++;
                break;
            default:
                break;
        }
    }

    static void deleteFromPw(char c) {
        switch (c) {
            case 'A':
                count[0]--;
                break;
            case 'C':
                count[1]--;
                break;
            case 'G':
                count[2]--;
                break;
            case 'T':
                count[3]--;
                break;
            default:
                break;
        }
    }

    static boolean isMatch(int[] criteria, int[] count) {
        boolean notMatch = false;
        for (int i = 0; i < 4; i++) {
            if (criteria[i] > count[i]) {
                notMatch = true;
                break;
            }
        }
        return !notMatch;
    }
}
