#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{ 
    // 균형잡힌 세상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    while (true) {
        string str;
        getline(cin, str);
        stack<char> stk;
        bool is_invalid = false;

        if (str[0] == '.') // 종료조건
            break;

        for (int i = 0; i < str.size(); i++) {
            if (str[i] == '.')
                break;
            if (str[i] == '(' || str[i] == '[')
                stk.push(str[i]);
            else if (str[i] == ')' && !stk.empty() && stk.top() == '(')
                stk.pop();
            else if (str[i] == ']' && !stk.empty() && stk.top() == '[')
                stk.pop();
            else if (str[i] == ' ' || ('a' <= str[i] && str[i] <= 'z') || ('A' <= str[i] && str[i] <= 'Z'))
                continue;
            else {
                is_invalid = true;
                break;
            }
        }

        if (!stk.empty() || is_invalid == true)
            cout << "no\n";
        else
            cout << "yes\n";
    }
    return 0;
}