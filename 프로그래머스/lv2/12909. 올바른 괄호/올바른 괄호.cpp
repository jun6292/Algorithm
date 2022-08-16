#include <string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> st;
    
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(')    // 스택에 '('만 push
            st.push(s[i]);
        else if (s[i] == ')' && !st.empty())    // 스택이 비어있지 않으면 '('가 있다는 의미
            st.pop();                           // 쌍이 맞았으므로 맨 위의 '(' 제거
        else if (s[i] == ')' && st.empty()) 
            return false;
    }
    if (!st.empty())    // for문 통과 후 stack이 비어있지 않으면 '('가 남았다는 의미
            return false;
    
    return answer;
}