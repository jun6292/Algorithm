import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char tmp = s.charAt(i);
            if (!map.containsKey(tmp)) {
                map.put(tmp, i);
                answer[i] = -1;
            } else {
                answer[i] = i - map.get(tmp);
                map.put(tmp, Math.max(i, map.get(tmp)));
            }
        }
        return answer;
    }
}