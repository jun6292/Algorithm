#include <string>
#include <vector>

using namespace std;

int solution(int left, int right) {
    int answer = 0;
    while (left <= right){
        int cnt = 0;    // number of factors
        int i = 1;
        while (i <= left){
            if (left % i == 0)
                cnt++;
            i++;
        }
        if (cnt % 2 == 0)   // 약수의 개수가 짝수인 수는 더하고, 홀수인 수는 뺀다
            answer += left;
        else
            answer -= left;
        left++;
    }
    return answer;
}