import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        Map<Character, Integer> keypad = new HashMap<Character, Integer>();
        for (int i = 0; i < keymap.length; i++) {
            for (int j = 0; j < keymap[i].length(); j++) {
                char ch = keymap[i].charAt(j);
                if (keypad.containsKey(ch)) {
                    keypad.put(ch, Math.min(keypad.get(ch), j + 1));
                }
                else {
                    keypad.put(ch, j + 1);
                }
            }
        }
        for (int i = 0; i < targets.length; i++) {
            int result = 0;
            boolean flag = true;
            for (int j = 0; j < targets[i].length(); j++) {
                if (keypad.containsKey(targets[i].charAt(j))) {
                    result += keypad.get(targets[i].charAt(j));
                }
                else {
                    flag = false;
                }
            }
            if (flag)
                answer[i] = result;
            else
                answer[i] = -1;
        }
        return answer;
    }
}