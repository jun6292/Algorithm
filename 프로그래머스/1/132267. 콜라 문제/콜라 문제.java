class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        int bottle, rest;
        while (n >= a) {
            answer += (n / a) * b;
            n = (n / a) * b + (n % a);
        }
        
        return answer;
    }
}