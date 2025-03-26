// https://school.programmers.co.kr/learn/courses/30/lessons/42895
// Referenced: https://small-stap.tistory.com/65

package git.daily_algorithm.programmers.L3;

import java.util.ArrayList;
import java.util.HashSet;

public class P42895 {
    public int solution(int N, int number) {
        if (N == number)
            return 1;

        // N은 8개까지 사용 가능하므로, 8개의 배열 생성
        ArrayList<HashSet<Integer>> setList = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            setList.add(new HashSet<>());
        }

        for (int i = 0; i < 8; i++) {
            int concat = 0;
            for (int j = 0; j <= i; j++) {
                concat = concat * 10 + N;
            }
            setList.get(i).add(concat);

            // 이전 단계들에서 만든 숫자들을 조합하여 새로운 수 추가
            for (int j = 0; j < i; j++) {
                for (int op1 : setList.get(j)) {
                    for (int op2 : setList.get(i - j - 1)) {
                        setList.get(i).add(op1 + op2);
                        setList.get(i).add(op1 - op2);
                        setList.get(i).add(op1 * op2);
                        if (op2 != 0) {
                            setList.get(i).add(op1 / op2);
                        }
                    }
                }
            }

            if (setList.get(i).contains(number)) {
                return i + 1;
            }
        }
        return -1;
    }
}