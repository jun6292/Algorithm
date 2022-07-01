#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> num;
    while (n){
        num.push_back(n % 3);
        n /= 3;
    }
    int idx = num.size() - 1;
    int pow = 1;
    while (idx > -1){
        answer += num[idx] * pow;
        idx--;
        pow *= 3;
    }
    return answer;
}