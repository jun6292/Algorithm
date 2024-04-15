import java.util.*;

class Solution {
    public int solution(int[] number) {
        int answer = 0;
        int arrLen = number.length;
        for (int i = 0; i < arrLen - 2; i++) {
            for (int j = i + 1; j < arrLen - 1; j++) {
                for (int k = j + 1; k < arrLen; k++) {
                    if (number[i] + number[j] + number[k] == 0) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}