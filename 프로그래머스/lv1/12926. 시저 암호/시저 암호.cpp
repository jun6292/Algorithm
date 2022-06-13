#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    string lowercase = "abcdefghijklmnopqrstuvwxyz";
    string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for(int i = 0; i < s.length(); i++){
        if ('a' <= s[i] && s[i] <= 'z')
            answer += lowercase[(s[i] - 'a' + n) % 26];  // 소문자 밀기
        else if ('A' <= s[i] && s[i] <= 'Z')
            answer += uppercase[(s[i] - 'A' + n) % 26];  // 대문자 밀기
        else
            answer += s[i]; // 공백
    }
    return answer;
}