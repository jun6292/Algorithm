class Solution {
    public int solution(String s) {
        int answer = 0;
        int cnt1 = 0, cnt2 = 0;
        char ch = s.charAt(0);
        boolean isNew = true;
        for (int i = 0; i < s.length(); i++) {
            if (isNew) {
                ch = s.charAt(i);
                cnt1++;
                isNew = false;
            } else {
                if (s.charAt(i) == ch) {
                    cnt1++;
                }
                else
                    cnt2++;
            }
            if (cnt1 == cnt2) {
                answer++;
                isNew = true;
                cnt1 = 0;
                cnt2 = 0;
            }
        }
        if (cnt1 >= 1 && !isNew)
            answer++;
        return answer;
    }
}