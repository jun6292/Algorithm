class Solution {
    public int solution(int n) {
        int answer = 0;
        String bitStr = Integer.toBinaryString(n); // n을 2진수 변환
        int bitCnt = 0;
        for (int i = 0;i< bitStr.length(); i++){
            if (bitStr.charAt(i) == '1') 
                bitCnt++;
        }
        
        for(int i = n + 1; i < 1000000; i++){
            String tmp = Integer.toBinaryString(i);
            int tempCnt = 0;
            for(int j = 0; j < tmp.length(); j++){
                if(tmp.charAt(j) == '1') tempCnt++;
            }
            // 1인 비트의 수가 일치하면 해당 수를 반환
            if(tempCnt == bitCnt) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}