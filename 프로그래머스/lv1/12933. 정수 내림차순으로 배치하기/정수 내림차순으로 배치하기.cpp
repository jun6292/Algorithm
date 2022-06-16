#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string s_num = to_string(n);
    sort(s_num.begin(), s_num.end(), greater<int>());
    answer = stoll(s_num);
    return answer;
}