#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    vector<string> num = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    vector<string> digit = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" };
    int idx;
    for (int i = 0; i < num.size(); i++) {
        while (1) {
            idx = s.find(num[i]);
            if (idx == string::npos)
                break;
            s.replace(idx, num[i].length(), digit[i]);
        }
    }
    answer = stoi(s);
    return answer;
}