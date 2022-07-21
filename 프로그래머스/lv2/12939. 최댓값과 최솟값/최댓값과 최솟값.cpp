#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

string solution(string s) {
    string answer = "";
    istringstream iss (s);
    string buf;
    vector<int> num;
    // 문자열을 공백 기준으로 잘라서 int형으로 변환 후 num 배열 넣는다.
    while (getline(iss, buf, ' ')) {
        num.push_back(stoi(buf));
    }
    // 오름차순 정렬
    sort(num.begin(), num.end());
    answer = to_string(num[0]) + " " + to_string(num[num.size() - 1]);
    return answer;
}