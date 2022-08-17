#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    // 괄호
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;           // 테스트 케이스
    string PS;          // 괄호 문자열 
    bool is_invalid;    // 괄호 문자열 판별, false가 Valid PS

    for (int i = 0; i < T; i++) {
        stack<char> st;
        cin >> PS;
        is_invalid = false;    

        for (int j = 0; j < PS.size(); j++) {
            if (PS[j] == '(')
                st.push(PS[j]);
            else if (PS[j] == ')' && !st.empty())
                st.pop();
            else if (PS[j] == ')' && st.empty()) {
                is_invalid = true;
                break;
            }
        }
        if (!st.empty() || is_invalid == true)
            cout << "NO\n";
        else
            cout << "YES\n";
    }
    return 0;
}