// https://school.programmers.co.kr/learn/courses/30/lessons/142086

package git.daily_algorithm.programmers.L1;

import java.util.HashMap;
import java.util.Map;

class P142086 {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];

        int idx = 0;
        Map<Character, Integer> charMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (charMap.get(c) == null) {
                charMap.put(c, idx);
                answer[idx] = -1;
            } else {
                int pos = charMap.get(c);
                answer[idx] = idx - pos;
                charMap.put(c, idx);
            }
            idx++;
        }

        // int[] charArr = new int['z' - 'a' + 1];
        // Arrays.fill(charArr, -1);
        
        // for (char c : s.toCharArray()) {
        //     int cIdx = c - 'a';
        //     if (charArr[cIdx] == -1) {
        //         answer[idx] = -1;
        //         charArr[cIdx] = idx;
        //     } else {
        //         int pos = charArr[cIdx];
        //         answer[idx] = idx - pos;
        //         charArr[cIdx] = idx;
        //     }
        //     idx++;
        // }

        return answer;
    }
}