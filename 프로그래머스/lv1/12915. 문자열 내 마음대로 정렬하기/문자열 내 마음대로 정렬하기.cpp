#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int N;  // compare 함수에 n값을 받아오는 용도로 선언
bool compare(string a, string b)
{
    if (a[N] == b[N])
        return a < b;
    else if (a[N] < b[N])
        return true;
    else
        return false;
}

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer = strings;
    N = n;
    sort(answer.begin(), answer.end(), compare);
    return answer;
}