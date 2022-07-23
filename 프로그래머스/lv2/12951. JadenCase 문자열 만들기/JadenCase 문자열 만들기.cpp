#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    if ('a' <= s[0] && s[0] <= 'z')
        answer += toupper(s[0]);
    else
        answer += s[0];
    for (int i = 1; i < s.size(); i++) {
        if (s[i - 1] == ' ' && s[i] != ' ')
            answer += toupper(s[i]);
        else
            answer += tolower(s[i]);
    }
    return answer;
}