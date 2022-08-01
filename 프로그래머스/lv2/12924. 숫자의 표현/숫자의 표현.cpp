#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1, j = 1;
    int sum = 0;
    if (n == 1)
        return answer;
    for (int i = 1; i <= (n + 1) / 2; i++) {
        sum += i;
        if (sum >= n) {
            while (sum > n) {
                sum -= j;
                j++;
            }
            if (sum == n)
                answer++;
        }
    }
    return answer;
}