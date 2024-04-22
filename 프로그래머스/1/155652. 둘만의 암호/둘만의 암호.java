import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        int n = 26 - skip.length();
        Character[] alphabet = new Character[n];
        int idx = 0;
        for (char ch = 'a'; ch <= 'z'; ch++) {
            if (!skip.contains(String.valueOf(ch))) {
                alphabet[idx] = ch;
                idx++;
            }
        }
        for (int i = 0; i < s.length(); i++) {
            int idx2 = Arrays.asList(alphabet).indexOf(s.charAt(i));
            answer = answer + alphabet[(idx2 + index) % n];
        }
        return answer;
    }
}