#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    long long n = num;
    int cnt = 0;    // count repetition
    while (true){
        if (n == 1)
            break;
        if (n % 2 == 0)
            n /= 2;
        else
            n = n * 3 + 1;
        cnt++;
        if (cnt >= 500)
            return -1;
    }
    answer = cnt;
    return answer;
}